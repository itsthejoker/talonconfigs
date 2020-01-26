from talon.voice import Key, Context

ctx = Context("pycharm", bundle="com.jetbrains.pycharm")

keymap = {
    "next tab": Key("shift-cmd-]"),
    "previous tab": Key("shift-cmd-["),
    "project": Key("cmd-1"),
    "editor": Key("esc"),
    "terminal": Key("alt-f12"),
    "inspect": Key("cmd-down"),
    "save": Key("cmd+s"),
    "preferences": Key("cmd-,"),
    "sort imports": Key("ctrl-alt-o"),
    "format lines": Key("cmd-alt-l"),
    "search all": Key("cmd-shift-f")
}

ctx.keymap(keymap)
