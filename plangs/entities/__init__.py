"""
Every entity that we create needs to either have a unique ID or belong to an entity with unique ID
(for ex: Logos don't have an id but are owned by an entity).
"""

from collections import defaultdict
from enum import Enum
from typing import Callable

from plangs.schema import Logo, Platform, ProgrammingLanguage, Paradigm, Typing


class IdLang(Enum):
    _ID: Callable[[str], str] = lambda lang: f"lang-{lang}"

    def set(self, lang: ProgrammingLanguage) -> None:
        ALL_LANGUAGES[self] = lang

    def get(self) -> ProgrammingLanguage:
        return ALL_LANGUAGES[self]

    PYTHON = _ID("python")
    ABC = _ID("abc")
    ADA = _ID("ada")
    ALGOL68 = _ID("algol68")
    APL = _ID("apl")
    BOO = _ID("boo")
    C = _ID("c")
    CPP = _ID("c++")
    CIRCUIT_PYTHON = _ID("circuit-python")
    CLU = _ID("clu")
    COBRA = _ID("cobra")
    COFFEE_SCRIPT = _ID("coffee-script")
    CPYTHON = _ID("cpython")
    CYTHON = _ID("cython")
    D = _ID("d")
    DYLAN = _ID("dylan")
    F_SHARP = _ID("f-sharp")
    GD_SCRIPT = _ID("gd-script")
    GENIE = _ID("genie")
    GO = _ID("go")
    GROOVY = _ID("groovy")
    HASKELL = _ID("haskell")
    ICON = _ID("icon")
    IRON_PYTHON = _ID("iron-python")
    JAVASCRIPT = _ID("javaScript")
    JULIA = _ID("julia")
    JYTHON = _ID("jython")
    LISP = _ID("lisp")
    MICRO_PYTHON = _ID("micro-python")
    MODULA_3 = _ID("modula-3")
    MOJO = _ID("mojo")
    NIM = _ID("nim")
    PERL = _ID("perl")
    PYPY = _ID("pypy")
    RING = _ID("ring")
    RPYTHON = _ID("rpython")
    RUBY = _ID("ruby")
    STACKLESS_PYTHON = _ID("stackless-python")
    STANDARD_ML = _ID("standard-ml")
    STARLARK = _ID("starlark")
    SWIFT = _ID("swift")


class IdParadigm(Enum):
    _ID: Callable[[str], str] = lambda para: f"para-{para}"

    def set(self, paradigm: Paradigm) -> None:
        ALL_PARADIGMS[self] = paradigm

    def get(self) -> Paradigm:
        return ALL_PARADIGMS[self]

    MULTI = _ID("multi-paradigm")
    OOP = _ID("object-oriented")
    PROCEDURAL = _ID("procedural")
    IMPERATIVE = _ID("imperative")
    FUNCTIONAL = _ID("functional")
    STRUCTURED = _ID("structured")
    REFLECTIVE = _ID("reflective")


class IdTyping(Enum):
    _ID: Callable[[str], str] = lambda para: f"typing-{para}"

    def set(self, paradigm: Typing) -> None:
        ALL_TYPINGS[self] = paradigm

    def get(self) -> Typing:
        return ALL_TYPINGS[self]

    DUCK_TYPING = _ID("duck")
    DYNAMIC_TYPING = _ID("dynamic")
    OPTIONAL_TYPYING = _ID("optional")


class IdPlatform(Enum):
    _ID: Callable[[str], str] = lambda para: f"platform-{para}"

    def set(self, paradigm: Platform) -> None:
        ALL_PLATFORMS[self] = paradigm

    def get(self) -> Platform:
        return ALL_PLATFORMS[self]

    WINDOWS = _ID("windows")
    MACOS = _ID("macos")
    LINUX = _ID("linux")
    ANDROID = _ID("android")
    BSD = _ID("bsd")
    WASM = _ID("wasm")


ALL_LANGUAGES: dict[IdLang, ProgrammingLanguage] = {}
ALL_PARADIGMS: dict[IdParadigm, Paradigm] = {}
ALL_TYPINGS: dict[IdTyping, Typing] = {}
ALL_PLATFORMS: dict[IdPlatform, Platform] = {}

# These entities don't have an ID but are owned by an entity.
ALL_LOGOS: dict[IdLang, list[Logo]] = defaultdict(list)


def _defaultName(basename: str) -> str:
    """Converts a snake_case string to a title case string."""
    return " ".join(map(lambda s: s.capitalize(), basename.split("_")))


# Create all the entities.
for idClass, schemaClass in (
    (IdLang, ProgrammingLanguage),
    (IdParadigm, Paradigm),
    (IdPlatform, Platform),
    (IdTyping, Typing),
):
    for val in idClass:
        instance = schemaClass(id=val.value, name=_defaultName(val.name))
        val.set(instance) # type: ignore