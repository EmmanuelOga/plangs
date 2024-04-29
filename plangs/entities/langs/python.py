from plangs.entities import ALL_LOGOS, IdLang, IdParadigm
from plangs.schema import Logo, ProgrammingLanguage


def create():
    lang_id = IdLang.PYTHON
    lang = lang_id.get()

    lang.paradigm_ids.extend(
        map(
            lambda p: p.value,
            [
                IdParadigm.MULTI,
                IdParadigm.OOP,
                IdParadigm.PROCEDURAL,
                IdParadigm.IMPERATIVE,
                IdParadigm.FUNCTIONAL,
                IdParadigm.STRUCTURED,
                IdParadigm.REFLECTIVE,
            ],
        )
    )

    ALL_LOGOS[lang_id].extend(
        [
            Logo(
                entity_id=lang_id.value,
                path="/langs/python/logos/python-logo-generic.svg",
                description="Python Logotype",
            ),
            Logo(
                entity_id=lang_id.value,
                path="/langs/python/logos/python-logo-only.svg",
                description="Python Logo",
            ),
        ]
    )


# releases = []
# designer = "people/v/van-rossum-guido"
# organization = "org/p/python-software-foundation"
# implementations = [
#     "cpython",
#     "pypy",
#     "stackless-python",
#     "micro-python",
#     "circuit-python",
#     "iron-python",
#     "jython",
# ]
# licenses = ... # from releases
# fileExt ...
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

