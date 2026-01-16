from schema import SCHEMA
from db import get_connection   

def inspect_schema() -> dict:
    """
    Returns authoritative dataset schema and data quality info.
    This is the only allowed source of truth for column existence.
    """
    return SCHEMA


def run_query(sql: str) -> list[dict]:
    """
    Executes a read-only SQL query against the dataset.
    Returns rows as a list of dicts.
    """
    con = get_connection()

    # Hard safety rule: read-only queries
    lowered = sql.lower()
    if any(word in lowered for word in ["insert", "update", "delete", "drop", "alter"]):
        raise ValueError("Only read-only SELECT queries are allowed.")

    result = con.execute(sql).fetchdf()
    return result.to_dict(orient="records")