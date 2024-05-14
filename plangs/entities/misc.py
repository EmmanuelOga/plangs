import duckdb
from plangs.phases import phase
from sourcetypes import sql  # type: ignore


@phase(0)
def create(conn: duckdb.DuckDBPyConnection):
    stmt: sql = """
    insert into paradigms (key, description)
    values
    ('para-oop', 'Object-Oriented'),
    ('para-imp', 'Imperative'),
    ('para-func', 'Functional'),
    ('para-struct', 'Structured'),
    ('para-refl', 'Reflective');
    """
    conn.execute(stmt)

    stmt: sql = """
    insert into type_systems (key)
    values
    ('types-duck'),
    ('types-dynamic'),
    ('types-strong'),
    ('types-optional');
    """
    conn.execute(stmt)

    stmt: sql = """
    insert into environments (key)
    values
    ('env-linux'),
    ('env-windows'),
    ('env-macos'),
    ('env-ios'),
    ('env-android'),
    ('env-wasm'),
    ('env-rpi');
    """
    conn.execute(stmt)
