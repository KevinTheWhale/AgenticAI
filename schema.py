# CREATE THE AGENT'S FIRST TOOL
# Obj: Turn documented schema into a callable function that the agent can USE instead of guessing. 
# "It knows the truth and this is the single source of the truth"
'''
- Agent never invents columns
- The Agent can refuses nonsense questions (initial guardrail)
- Every answer can cite known data limitations
'''

# BASED OFF OUTPUT FROM UniAgent.py -> Metadata storage
SCHEMA = { 
    "row_count": 7260,
    "columns": {
        "id": {"type": "VARCHAR", "null_rate": 0.0},
        "name": {"type": "VARCHAR", "null_rate": 0.00386},
        "level": {"type": "BIGINT", "null_rate": 0.00110},
        "exp": {"type": "BIGINT", "null_rate": 0.18347},
        "boss": {"type": "BIGINT", "null_rate": 0.0},
        "HP": {"type": "BIGINT", "null_rate": 0.00647},
        "MP": {"type": "BIGINT", "null_rate": 0.03967},
        "exp_div_hp": {"type": "DOUBLE", "null_rate": 0.18926},
    }
}