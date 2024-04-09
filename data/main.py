import paradigms  # noqa: F401
import langs.p.python  # noqa: F401
import kuzu
import shutil
import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


def createDB():
    """Create a new database. Removes the old one if it exists."""
    path = os.path.join(ROOT_DIR, "db")
    shutil.rmtree(path, ignore_errors=True)
    db = kuzu.Database(path, buffer_pool_size=1024**3)
    return db


def createConnection(db):
    return kuzu.Connection(db)


if __name__ == "__main__":
    conn = createConnection(createDB())

    with open(os.path.join(ROOT_DIR, "cypher/schema.cypher"), "r") as schema:
        conn.execute(schema.read())

    conn.execute("CREATE (:Person {name: 'Alice', age: 25});")
    conn.execute("CREATE (:Person {name: 'Bob', age: 30});")

    result = conn.execute("MATCH (a:Person) RETURN a.name AS NAME, a.age AS AGE;")
    while result.has_next():
        row = result.get_next()
        print(row)
