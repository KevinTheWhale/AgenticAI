# HOW THE AGENT INTERPRETS IT INTO NATURAL LANGUAGE
from schema import SCHEMA

def build_explanation(sql: str, result_rows: int) -> dict:
    """
    Builds an explainability block for an executed query.
    """
    caveats = []

    # Null-rate caveats
    for col, meta in SCHEMA["columns"].items():
        if meta["null_rate"] > 0.10:
            caveats.append(
                f"Column '{col}' has {meta['null_rate']:.1%} missing values."
            )

    explanation = {
        "method": f"Computed results using SQL: {sql.strip()}",
        "data_used": f"{result_rows} rows returned out of {SCHEMA['row_count']} total rows",
        "caveats": caveats
    }

    return explanation