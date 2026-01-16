# Rule-based agent (no LLM yet)
from tools import inspect_schema, run_query # give agent the tools
from schema import SCHEMA # give agent the guardrails and full context of the data

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
    is_valid, reason = validate_question(question)

    if not is_valid:
        return {
            "action": "refuse",
            "reason": reason,
            "schema": inspect_schema()
        }

    # For now: simple heuristic
    if "schema" in question.lower() or "columns" in question.lower():
        return {
            "action": "inspect_schema",
            "result": inspect_schema()
        }

    # Placeholder SQL (will be LLM-generated next step)
    sql = """
    SELECT name, level, exp
    FROM data
    ORDER BY exp DESC
    LIMIT 5
    """

    return {
        "action": "run_query",
        "sql": sql,
        "result": run_query(sql)
    }