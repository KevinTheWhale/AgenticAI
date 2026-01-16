import duckdb

# TURN RAW CSV INTO A STRUCTURED "TABLE" AND SUMMARIZE CONTENTS -> Use output as the authoritative schema context for your agent
CSV_PATH = "CompleteDatabase.csv"  # Should be dynamic to any dataset (or at least most?)

con = duckdb.connect() # connect database for the data warehouse

# Load CSV as a table-like view: (I need to know what it looks like for context)
con.execute(f"""
CREATE OR REPLACE VIEW data AS
SELECT * FROM read_csv_auto('{CSV_PATH}', header=True);
""") # Duck reads the CSV and automatically detects the column types
# 'CREATE VIEW data' = Gives that CSV the name 'data' to give SQL cmd capabilities

rows = con.execute("SELECT COUNT(*) FROM data").fetchone()[0] # Row count - How many records are in the dataset
cols = con.execute("DESCRIBE data").fetchall()  # (column_name, column_type, null, key, default, extra), return col metadata

print(f"\nRows: {rows}\n")
print("Columns (name : type : null_rate)")
for name, coltype, *_ in cols: # investigate and find NULL values in each column to prevent hallucinations from missing content
    # Quote the column safely
    q = f'SELECT AVG(CASE WHEN "{name}" IS NULL THEN 1 ELSE 0 END) FROM data'
    null_rate = con.execute(q).fetchone()[0]
    print(f"- {name} : {coltype} : {null_rate:.3%}")


