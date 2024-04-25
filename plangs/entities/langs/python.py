from plangs.entities.decorators import creates_entities, creates_relationships
from plangs.entities import IdLang, IdParadigm
from plangs.schema import ProgrammingLanguage


@creates_entities
def create():
    id = IdLang.PYTHON
    lang = ProgrammingLanguage(
        id=id.value,
        name="Python",
        logo="/logos/p/python/python-logo-generic.svg",
    )
    id.set(lang)


@creates_relationships
def relate():
    lang = IdLang.PYTHON.get()
    lang.paradigms.extend(
        [
            IdParadigm.MULTI.get(),
            IdParadigm.OOP.get(),
            IdParadigm.PROCEDURAL.get(),
            IdParadigm.IMPERATIVE.get(),
            IdParadigm.FUNCTIONAL.get(),
            IdParadigm.STRUCTURED.get(),
            IdParadigm.REFLECTIVE.get(),
        ]
    )


# releases = []
# designer = "people/v/van-rossum-guido"
# developer = "org/p/python-software-foundation"
# typing = [
#     "duck-typing",
#     "dynamic-typing",
#     "optional-typying",
# ]
# implementations = [
#     "cpython",
#     "pypy",
#     "stackless-python",
#     "micro-python",
#     "circuit-python",
#     "iron-python",
#     "jython",
# ]
# operatingSystems = [
#     "windows",
#     "macos",
#     "linux",
#     "android",
#     "bsd",
# ]
# licenses = "licenses/python/*.ent"
# fileExt = "licenses/py/*.ent"
# urls = ["https=//python.org"]
# dialects = [
#     "cython",
#     "pypy",
#     "rpython",
#     "starlark",
# ]
# influencedBy = [
#     "abc",
#     "ada",
#     "algol68",
#     "apl",
#     "c",
#     "c++",
#     "clu",
#     "dylan",
#     "haskell",
#     "icon",
#     "lisp",
#     "modula-3",
#     "perl",
#     "standard-ml",
# ]
# influenced = [
#     "groovy",
#     "boo",
#     "cobra",
#     "coffee-script",
#     "d",
#     "f-sharp",
#     "gd-script",
#     "genie",
#     "go",
#     "javaScript",
#     "julia",
#     "mojo",
#     "nim",
#     "ring",
#     "ruby",
#     "swift",
# ]
