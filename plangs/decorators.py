from typing import Callable


def creates_entities(func: Callable[[], None]) -> Callable[[], None]:
    """Track functions that define entities."""
    ENTITY_CREATORS.append(func)
    return func


def creates_relationships(func: Callable[[], None]) -> Callable[[], None]:
    """Track functions that define relationships."""
    RELATIONSHIP_CREATORS.append(func)
    return func


def invoke_entity_creators():
    """Invoke all functions that define entities and relationships."""
    for creator in ENTITY_CREATORS:
        creator()


def invoke_relationship_creators():
    """Invoke all functions that define entities and relationships."""
    for creator in RELATIONSHIP_CREATORS:
        creator()


ENTITY_CREATORS: list[Callable[[], None]] = []
RELATIONSHIP_CREATORS: list[Callable[[], None]] = []
