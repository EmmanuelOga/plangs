from pydantic import BaseModel


class ProgrammingLanguage(BaseModel):
    id: str
    name: str
    paradigm_ids: list[str] = []


class Paradigm(BaseModel):
    id: str
    name: str


class Platform(BaseModel):
    id: str
    name: str


class Typing(BaseModel):
    id: str
    name: str


class Logo(BaseModel):
    entity_id: str
    path: str
    description: str = ""
