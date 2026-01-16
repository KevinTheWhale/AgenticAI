from schema import SCHEMA

def inspect_schema() -> dict:
    """
    Returns authoritative dataset schema and data quality info.
    This is the only allowed source of truth for column existence.
    """
    return SCHEMA