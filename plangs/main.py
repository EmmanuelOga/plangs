import importlib
from glob import iglob

from plangs import ROOT_PATH

def load_all_entities():
    """
    Import every module under the entities directory.
    This should populate all the functions that define entities and relationships.
    """
    path = ROOT_PATH / "plangs/entities/**/*.py"
    prefix = ROOT_PATH.as_posix()
    for modpath in iglob(path.as_posix()):
        mod = modpath.split(prefix)[-1].replace("/", ".").replace("\\", ".")[1:-3]
        importlib.import_module(mod)


if __name__ == "__main__":
    load_all_entities()

    print("READY.")
