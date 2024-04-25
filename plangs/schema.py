from pydantic import BaseModel


class ProgrammingLanguage(BaseModel):
    id: str
    name: str
    logo: str | None = None
    paradigms: list["Paradigm"] = []


class Paradigm(BaseModel):
    id: str
    name: str
