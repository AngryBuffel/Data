from duckdb import connect

class SQL:
    def __init__(self, sql, **bindings):
        self.sql = sql
        self.bindings = bindings

class DuckDB:
    def __init__(self, options=""):
        self.options = options

    def query(self, select_statement: SQL):
        db = connect(":memory:")
        db.query("install httpfs; load httpfs;")
        db.query(self.options)

        dataframes = collect_dataframes(select_statement)
        for key, value in dataframes.items():
            db.register(key, value)

        result = db.query(sql_to_string(select_statement))
        if result is None:
            return
        return result.df()