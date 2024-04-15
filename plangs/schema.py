from pydantic import BaseModel


class ProgrammingLanguage(BaseModel):
    name: str
    logo: str | None = None
    paradigms: list["Paradigm"] = []


class Paradigm(BaseModel):
    name: str
