from openai import OpenAI
from models import AgentDecision
from schema import SCHEMA
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm_decide(question: str) -> AgentDecision:
    schema_desc = ", ".join(SCHEMA["columns"].keys())

    prompt = f"""
You are a data analysis agent.

Dataset table name: data
Dataset columns: {schema_desc}

Rules:
- ALWAYS query from the table named "data"
- Only reference existing columns
- Only generate SELECT queries
- Respond ONLY in valid JSON
- If the question references unknown data, refuse

Return JSON in this format:
{{
  "action": "run_query | inspect_schema | refuse",
  "sql": "... or null",
  "reason": "... or null"
}}

Question: {question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    content = response.choices[0].message.content
    return AgentDecision.model_validate_json(content)