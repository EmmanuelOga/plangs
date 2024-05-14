import importlib
import os
from collections import defaultdict
from typing import Any, Callable

from plangs import ROOT_PATH

PHASES: dict[int, list[Callable[..., None]]] = defaultdict(list)

def phase(n: int):
    """
    Decorator to mark a function as part of a phase.

    @phase(42)
    def func(args):
        pass
    """

    def decorator(func : Callable[..., None]):
        PHASES[n].append(func)
        return func

    return decorator


def execute_phase(n: int, *args: Any, **kwargs: Any):
    """
    Execute all functions marked with the phase decorator, sending the given arguments.
    """
    for func in PHASES[n]:
        func(*args, **kwargs)


def load_all_entities():
    """
    Import every module under the entities directory.
    This should populate all the functions that define entities and relationships.
    """
    for modpath in (ROOT_PATH / "plangs" / "entities").rglob("*.py"):
        path = f"{modpath.relative_to(ROOT_PATH)}".split(os.sep)
        modname = (".".join(path))[:-3]
        importlib.import_module(modname)
