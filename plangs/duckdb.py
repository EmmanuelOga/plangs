import re
from dataclasses import dataclass
from pathlib import Path

import duckdb

STATEMENT_NAME_RE = re.compile(r"^--\s*(\w+)\s*$")


@dataclass
class SqlSourceStatement:
    """
    Holds a piece of SQL extracted from a file,
    with pointers to the the file and line number.
    """

    path: Path
    lineno: int
    sql: str

    def find_name(self) -> str | None:
        """
        Find a comment in the SQL that names the statement, if any.
        """
        for line in self.sql.splitlines():
            if match := re.match(STATEMENT_NAME_RE, line):
                if match.group(1):
                    return match.group(1)

    def exec(self, conn: duckdb.DuckDBPyConnection):
        """
        Excute a statement on a connection, or raise an error with the statement's info.
        """
        try:
            conn.execute(self.sql)
        except duckdb.Error as e:
            raise duckdb.Error(self) from e

    def __str__(self):
        return "from {self.path.absolute()}:{self.lineno}\n\n{self.sql}"


def load_statements(path: Path) -> list[SqlSourceStatement]:
    """
    Load SQL statements from a sql file.
    Statements should be separated by a semicolon.
    """
    statements: list[SqlSourceStatement] = []

    sql_parts = path.read_text().split(";")

    # Find the first line numbers for each part.
    line_numbers = [1]
    for i in range(1, len(sql_parts)):
        line_numbers.append(line_numbers[i - 1] + sql_parts[i - 1].count("\n") + 1)

    for i, sql in enumerate(sql_parts):
        statements.append(SqlSourceStatement(path, line_numbers[i], sql))

    return statements


def load_named_statements(path: Path) -> dict[str, SqlSourceStatement]:
    """
    Converts the list of statements loaded from the path into a dictionary.
    Each statement will be indexed only if prefixed by a comment with the name for it.

    Example file contents:

        -- stmt1
        SELECT * FROM table1;

        -- stmt2
        SELECT * FROM table2;

    """
    result: dict[str, SqlSourceStatement] = {}
    for stmt in load_statements(path):
        if name := stmt.find_name():
            result[name] = stmt
    return result
