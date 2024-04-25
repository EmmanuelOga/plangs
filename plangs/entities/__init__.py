from enum import Enum
from typing import Callable

from plangs.schema import ProgrammingLanguage, Paradigm


class IdLang(Enum):
    _ID: Callable[[str], str] = lambda lang: f"pl-{lang}"

    def set(self, lang: ProgrammingLanguage) -> None:
        ALL_LANGUAGES[self] = lang

    def get(self) -> ProgrammingLanguage:
        return ALL_LANGUAGES[self]

    PYTHON = _ID("python")


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


ALL_LANGUAGES: dict[IdLang, ProgrammingLanguage] = {}
ALL_PARADIGMS: dict[IdParadigm, Paradigm] = {}