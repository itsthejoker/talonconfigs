from talon.voice import Context, Key, Str

from ..text.formatters import FormatText
from ..text.formatters import formatters

context = Context("python")

def snaketext(m):
    # I can't figure out how to just pass in a formatter now that it's all
    # one magic object.
    f = []

    for i, word in enumerate(str(m.dgndictation).split()):
        f.append(formatters['snake'][1](i, word, i))

    Str(''.join(f))(None)


# def format_test(m):
#     print(m._words)
#     Str(FormatText(m))(None)

context.keymap(
    {
        "empty dict": "{}",
        "word (dickt | dictionary)": "dict",
        "state (def | deaf | deft)": "def ",
        "state else if": "elif ",
        "state if": "if ",
        "state while": ["while ()", Key("left")],
        "state for": "for ",
        "state switch": ["switch ()", Key("left")],
        "state case": ["case \nbreak;", Key("up")],
        "state goto": "goto ",
        "state import": "import ",
        "state class": "class ",
        "state include": "#include ",
        "state include system": ["#include <>", Key("left")],
        "state include local": ['#include ""', Key("left")],
        "state type deaf": "typedef ",
        "state type deaf struct": ["typedef struct {\n\n};", Key("up"), "\t"],
        "comment py": "# ",
        "dunder in it": "__init__",
        "self taught": "self.",
        "from import": ["from import ", Key("alt-left"), Key("space"), Key("left")],
        "for in": ["for in ", Key("alt-left"), Key("space"), Key("left")],
        "set trace": "import ipdb; ipdb.set_trace()",
        "start function <dgndictation> [over]": ["def ", snaketext, "():", Key("left"), Key("left")],
        # "start class <dgndictation> [over]": ['class ', smash_title_text, "():", Key("left"), Key("left")],
    }
)


