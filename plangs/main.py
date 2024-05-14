import duckdb

from plangs import ROOT_PATH
from plangs.duckdb import execute_sql
from plangs.phases import execute_phase, load_all_entities

if __name__ == "__main__":
    load_all_entities()

    print("Starting DuckDB ...")

    with duckdb.connect(":memory:") as conn:  # type: ignore
        execute_sql(conn, ROOT_PATH / "db" / "sql" / "schema.sql")

        execute_phase(0, conn)
        execute_phase(1, conn)

        result = conn.sql("SELECT * FROM languages")  # type: ignore
        result.show()
