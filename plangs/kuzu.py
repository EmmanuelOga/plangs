import shutil

import kuzu

from plangs import ROOT_PATH


def createDB(remove_existing: bool = True) -> kuzu.Database:
    """Create a new database."""
    path = ROOT_PATH / "data/kuzu"
    if remove_existing:
        shutil.rmtree(path, ignore_errors=True)
    path.mkdir(parents=True, exist_ok=True)
    db = kuzu.Database(path, buffer_pool_size=1024**3)
    return db

if __name__ == "__main__":
    pass
    # conn = createConnection(createDB())
    # with open(os.path.join(ROOT_DIR, "cypher/schema.cypher"), "r") as schema:
    #     conn.execute(schema.read())