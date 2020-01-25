from time import sleep

from talon.voice import Key, press, Str, Context, Rep, talon
from ..utils import parse_word, numerals, optional_numerals, text_to_number, jump_to_target

ctx = Context("generic_editor")

# actions and helper functions
def jump_to_bol(m):
    line = text_to_number(m)
    press("ctrl-g")
    Str(str(line))(None)
    press("enter")


def jump_to_end_of_line():
    press("cmd-right")


def jump_to_beginning_of_text():
    press("cmd-left")


def jump_to_nearly_end_of_line():
    press("left")


def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        else:
            press("ctrl-a")
            press("cmd-left")
        then()

    return fn


def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        press("cmd-right")
        then()

    return fn


def toggle_comments(*unneeded):
    press("cmd-/")


def snipline():
    press("ctrl-shift-k")


def get_first_word(m):
    return m.dgndictation.words[0]

def jump_to(m):
    target = get_first_word(m)
    jump_to_target(target)

def jump_to_line(m):
    if str(m) == "spring":
        return
    words = str(m).split()
    words.pop(0)
    words = int(''.join(words))
    press("ctrl-shift-up")
    press("cmd-pageup")
    for _ in range(words-1):
        press("down")
    press("ctrl-shift-.")

keymap = {
    "(trundle | comment)": toggle_comments,
    "(trundle | comment)"
    + numerals(): jump_to_bol_and(toggle_comments),  # noop for plain/text
    "snipline" + optional_numerals(): jump_to_bol_and(snipline),
    "sprinkle" + optional_numerals(): jump_to_bol,
    # "spring" + optional_numerals(): jump_to_eol_and(jump_to_beginning_of_text),
    "spring" + optional_numerals(): jump_to_line,
    "sprinkoon" + numerals(): jump_to_eol_and(lambda: press("enter")),
    "dear" + optional_numerals(): jump_to_eol_and(lambda: None),
    "smear" + optional_numerals(): jump_to_eol_and(jump_to_nearly_end_of_line),
    # general
    "fullscreen": Key("ctrl-cmd-f"),
    # file
    # "new": Key("cmd-n"),
    "(save | safe)": Key("cmd-s"),
    "close (file | tab)": Key("cmd-w"),
    # selection
    "(select | cell) up": Key("shift-up"),
    "(select | cell) down": Key("shift-down"),
    "(select | cell) all": Key("cmd-a"),
    "(select | cell) bottom ": Key("cmd-shift-down"),
    "(select | cell) right": Key("shift-right"),
    "(select | cell) left": Key("shift-left"),
    "(select | cell) word": Key("shift-alt-left"),
    "(select | cell) (end | push)": Key("cmd-shift-right"),
    "(select | cell) (start | begin | pop)": Key("cmd-shift-left"),
    # edit
    "paste match": Key("cmd-shift-v"),
    "tug": [Key("shift-end"), Key('shift-tab'), Key('escape')],
    "pull": [Key("shift-end"), Key('tab'), Key('escape')],
    "(scrap | scratch | delete) word": Key("alt-backspace"),
    "(scrap | scratch | delete) (begin | start)": Key("cmd-backspace"),
    # navigation
    "push": Key("cmd-right"),
    "pop": Key("cmd-left"),
    "jump": Key("alt-right"),
    "opjump": Key("alt-left"),
    "jump to <dgndictation>": jump_to,
    "junk": Key("backspace"),
    "home": Key("home"),
    "end": Key("end"),
}

ctx.keymap(keymap)
