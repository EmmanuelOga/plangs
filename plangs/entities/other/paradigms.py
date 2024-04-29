from plangs.entities import IdParadigm
from plangs.schema import Paradigm


def create():
    def create_paradigm(id: IdParadigm, name: str):
        id.set(Paradigm(id=id.value, name=name))

    create_paradigm(IdParadigm.MULTI, "Multi-Paradigm")
    create_paradigm(IdParadigm.OOP, "Object-Oriented")
    create_paradigm(IdParadigm.PROCEDURAL, "Procedural")
    create_paradigm(IdParadigm.IMPERATIVE, "Imperative")
    create_paradigm(IdParadigm.FUNCTIONAL, "Functional")
    create_paradigm(IdParadigm.STRUCTURED, "Structured")
    create_paradigm(IdParadigm.REFLECTIVE, "Reflective")
