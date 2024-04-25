import importlib
import os
import shutil
from glob import iglob

import kuzu

from plangs.decorators import invoke_entity_creators, invoke_relationship_creators
from plangs.entities import IdLang

ROOT_DIR: str = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
)


def createDB(remove_existing: bool = True) -> kuzu.Database:
    """Create a new database."""
    path = os.path.join(ROOT_DIR, "db")
    if remove_existing:
        shutil.rmtree(path, ignore_errors=True)
    db = kuzu.Database(path, buffer_pool_size=1024**3)
    return db


def load_all_entities():
    """
    Import every module under the entities directory.
    This should populate all the functions that define entities and relationships.
    """
    path = os.path.join(ROOT_DIR, "plangs/entities/**/*.py")
    for modpath in iglob(path):
        mod = modpath.split(ROOT_DIR)[-1].replace("/", ".").replace("\\", ".")[1:-3]
        importlib.import_module(mod)


if __name__ == "__main__":
    # conn = createConnection(createDB())

    # with open(os.path.join(ROOT_DIR, "cypher/schema.cypher"), "r") as schema:
    #     conn.execute(schema.read())

    load_all_entities()
    invoke_entity_creators()
    invoke_relationship_creators()

    print(IdLang.PYTHON.get().model_dump_json(indent=2))
