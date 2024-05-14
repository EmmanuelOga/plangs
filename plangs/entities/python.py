import duckdb
from plangs.phases import phase
from sourcetypes import sql  # type: ignore

KEY = "lang-python"


@phase(0)
def create(conn: duckdb.DuckDBPyConnection):
    desc = (
        "Python is a high-level, general-purpose programming language."
        + " Its design philosophy emphasizes code readability"
        + " with the use of significant indentation."
    )

    stmt: sql = """
        insert into languages (key, version, name, description)
        values
        ($1, '2', 'Python 2', $2),
        ($1, '3', 'Python 3', $2),
    """
    conn.execute(stmt, [KEY, desc])

    stmt: sql = """
        insert into languages (key, version, name, description)
        values
        ('lang-cython', '3', 'Cython 3',
            'Cython is a superset of the programming language Python, ' ||
            'which allows developers to write Python code ' ||
            '(with optional, C-inspired syntax extensions) ' ||
            'that yields performance comparable to that of C.'),
        ('lang-rpython', '0', 'RPython', ''),
        ('lang-starlark', '0', 'Starlark', '');
    """
    conn.execute(stmt)

    stmt: sql = """
    insert into people (key, full_name)
    values
    ('people-guido', 'Guido van Rossum');
    """
    conn.execute(stmt)


@phase(1)
def relate(conn: duckdb.DuckDBPyConnection):
    for ver in ["2", "3"]:
        stmt: sql = """
            insert into language_people (language, version, person)
            values
            ($py, $ver, 'people-guido');
        """
        conn.execute(stmt, {"py": KEY, "ver": ver})

        stmt: sql = """
            insert into language_paradigms (language, version, paradigm)
            values
            ($py, $ver, 'para-oop'),
            ($py, $ver, 'para-imp'),
            ($py, $ver, 'para-func');
        """
        conn.execute(stmt, {"py": KEY, "ver": ver})

    stmt: sql = """
        insert into implementations (key)
        values
        ('impl-cpython'),
        ('impl-pypy'),
        ('impl-stacklesspy'),
        ('impl-micropython'),
        ('impl-circuitpython'),
        ('impl-ironpython'),
        ('impl-jython');
    """
    conn.execute(stmt)
