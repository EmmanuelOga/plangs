import duckdb
from sourcetypes import sql  # type: ignore

from plangs.duckdb import paired_sql
from plangs.phases import phase

KEY = "lang-python"
SQL = paired_sql(__file__)


@phase(0)
def create(conn: duckdb.DuckDBPyConnection):
    desc = (
        "Python is a high-level, general-purpose programming language."
        + " Its design philosophy emphasizes code readability"
        + " with the use of significant indentation."
    )

    insl = SQL["insert-lang"]
    insl.exec(conn, {"key": KEY, "version": "2", "name": "Python 2", "desc": desc})
    insl.exec(conn, {"key": KEY, "version": "3", "name": "Python 3", "desc": desc})

    desc = (
        "Cython is a superset of the programming language Python, "
        + "which allows developers to write Python code "
        + "(with optional, C-inspired syntax extensions) "
        + "that yields performance comparable to that of C."
    )
    insl.exec(
        conn, {"key": "lang-cython", "version": "3", "name": "Cython", "desc": desc}
    )

    insl.exec(
        conn, {"key": "lang-rpython", "version": "0", "name": "RPython", "desc": ""}
    )
    insl.exec(
        conn, {"key": "lang-starlark", "version": "0", "name": "Starlark", "desc": ""}
    )

    insp = SQL["insert-people"]
    insp.exec(conn, {"key": "people-guido", "full_name": "Guido van Rossum"})


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
