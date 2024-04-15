from pprint import pprint
import kuzu
import shutil
import os

from langs.python import LangPython

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def createDB() -> kuzu.Database:
    """Create a new database. Removes the old one if it exists."""
    path = os.path.join(ROOT_DIR, "db")
    shutil.rmtree(path, ignore_errors=True)
    db = kuzu.Database(path, buffer_pool_size=1024**3)
    return db


def createConnection(db: kuzu.Database) -> kuzu.Connection:
    return kuzu.Connection(db)


if __name__ == "__main__":
    conn = createConnection(createDB())

    with open(os.path.join(ROOT_DIR, "cypher/schema.cypher"), "r") as schema:
        conn.execute(schema.read())

    pprint(LangPython.model_dump())

