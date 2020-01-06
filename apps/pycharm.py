from talon.voice import Key, Context

ctx = Context("pycharm", bundle="com.jetbrains.pycharm")

keymap = {
    "next tab": Key("shift-cmd-]"),
    "previous tab": Key("shift-cmd-["),
    "project": Key("cmd-1"),
    "editor": Key("esc"),
    "terminal": Key("alt-f12"),
    "inspect": Key("cmd-down"),
}

ctx.keymap(keymap)
