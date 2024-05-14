from pathlib import Path

import duckdb

from plangs.duckdb import SqlSourceStatement, load_named_statements
from plangs.phases import phase

SQL: dict[str, SqlSourceStatement] = load_named_statements(
    Path(__file__).with_suffix(".sql")
)


@phase(0)
def create(conn: duckdb.DuckDBPyConnection):
    SQL["paradigms"].exec(conn)
    SQL["type_systems"].exec(conn)
    SQL["environments"].exec(conn)
