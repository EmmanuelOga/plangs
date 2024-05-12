from pathlib import Path

import duckdb
from rich import inspect

from plangs import ROOT_PATH


def execute_sql(conn: duckdb.DuckDBPyConnection, sql_path: Path):
    """
    Reads the sql from the file and executes it on the connection,
    statement by statement (separated by ';') for error reporting.
    """
    with open(sql_path, "r") as file:
        sql_content = file.read()

    # Keep track of line numbers for error reporting.
    # TODO: maybe refactor to read the file line by line instead of loading it all at once.
    sql_parts = sql_content.split(";")
    line_numbers = [1]  # Start with line number 1
    for i in range(1, len(sql_parts)):
        line_numbers.append(line_numbers[i - 1] + sql_parts[i - 1].count("\n") + 1)

    # Run SQL statement by statement, but bail out on the first error.
    for i, sql_part in enumerate(sql_parts):
        try:
            conn.execute(sql_part)
        except duckdb.Error as e:
            raise Exception(
                {
                    "path": f"{sql_path.absolute()}:{line_numbers[i]}",
                    "sql": sql_part,
                    "error": e,
                }
            ) from e


if __name__ == "__main__":
    print("Starting DuckDB ...")

    try:
        with duckdb.connect(":memory:") as conn:  # type: ignore
            execute_sql(conn, ROOT_PATH / "db" / "sql" / "schema.sql")
            execute_sql(conn, ROOT_PATH / "db" / "sql" / "data.sql")

            result = conn.sql("SELECT * FROM typings")  # type: ignore
            result.show()
    except Exception as e:
        inspect(e)
