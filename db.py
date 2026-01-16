# DB HELPER -> Give the agent one controlled way to run analysis
import duckdb

CSV_PATH = "CompleteDatabase.csv"

_con = None

# single connection, single table with data
def get_connection():
    global _con
    if _con is None:
        _con = duckdb.connect()
        _con.execute(f"""
        CREATE OR REPLACE VIEW data AS
        SELECT * FROM read_csv_auto('{CSV_PATH}', header=True);
        """)
    return _con