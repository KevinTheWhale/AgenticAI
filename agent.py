# Rule-based agent (no LLM yet)
from tools import inspect_schema, run_query # give agent the tools
from schema import SCHEMA # give agent the guardrails and full context of the data
# Implement "brain" for agent
from models import AgentDecision
from llm import llm_decide
from explain import build_explanation


# Question validation (Critical guardrail) -> Avoids vague questions (i.e. "What's interesting here?")
def validate_question(question: str) -> tuple[bool, str]:
    """
    Checks whether the question references known columns.
    Returns (is_valid, reason).
    """
    known_columns = set(SCHEMA["columns"].keys())
    tokens = question.replace(",", " ").replace("?", " ").split()

    referenced = {t for t in tokens if t in known_columns}

    if not referenced:
        return False, "Question does not reference any known dataset columns."

    return True, ""



# Answering question
'''
- Agent chooses an action 
- Tools execute the action
- Results are returned without explanation yet
'''
def answer_question(question: str):
    # 1. Hard guardrail (never removed, gotta make sure we stay in scope)
    is_valid, reason = validate_question(question)
    if not is_valid:
        return {
            "action": "refuse",
            "reason": reason,
            "schema": inspect_schema()
        }

    # 2. Let the LLM propose an action
    decision: AgentDecision = llm_decide(question)

    # 3. Enforce allowed actions
    if decision.action == "refuse":
        return {
            "action": "refuse",
            "reason": decision.reason
        }

    if decision.action == "inspect_schema":
        return {
            "action": "inspect_schema",
            "result": inspect_schema()
        }

    if decision.action == "run_query":
        rows = run_query(decision.sql)
        explanation = build_explanation(
        sql=decision.sql,
        result_rows=len(rows)
        )

        return {
            "action": "run_query",
            "sql": decision.sql,
            "result": rows,
            "explanation": explanation
        }

    # 4. Safety fallback (should never happen, at least ideally)
    return {
        "action": "refuse",
        "reason": "Unrecognized agent action."
    }


