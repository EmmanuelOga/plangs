import duckdb

from plangs.duckdb import paired_sql
from plangs.phases import phase

SQL = paired_sql(__file__)


@phase(0)
def create(conn: duckdb.DuckDBPyConnection):
    SQL["paradigms"].exec(conn)
    SQL["type-systems"].exec(conn)
    SQL["environments"].exec(conn)
