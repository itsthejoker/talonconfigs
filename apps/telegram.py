from talon.voice import Key, Context

ctx = Context("telegram", bundle="com.tdesktop.Telegram")

keymap = {
    "channel down": Key("alt-down"),
    "channel up": Key("alt-up"),
    "send": Key("enter"),
}

ctx.keymap(keymap)
