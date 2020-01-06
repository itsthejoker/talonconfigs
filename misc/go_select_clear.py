from talon.voice import Context, Key
from os import system

ctx = Context('go-select-clear')

direction = 'right'
def set_dir(d):
    def wrapper(m):
        global direction
        direction = d
    return wrapper

ctx.keymap({
    # moving

    # left, right, up and down already defined
    'go word left': Key('alt-left'),
    'go word right': Key('alt-right'),

    'go left': Key('left'),
    'go right': Key('right'),
    'go up': Key('up'),
    'go down': Key('down'),

    'go line start': Key('cmd-left'),
    'go line end': Key('cmd-right'),

    'go way left': Key('cmd-left'),
    'go way right': Key('cmd-right'),
    'go way down': Key('cmd-down'),
    'go way up': Key('cmd-up'),

    # selecting
    'select line': Key('cmd-left cmd-left cmd-shift-right'),

    'select left': Key('shift-left'),
    'select right': Key('shift-right'),
    'select up': Key('shift-up'),
    'select down': Key('shift-down'),

    'select word left': [Key('left shift-right left alt-left alt-right shift-alt-left'), set_dir('left')],
    'select word right': [Key('right shift-left right alt-right alt-left shift-alt-right'), set_dir('right')],

    'extend': lambda m: Key(f'shift-alt-{direction}')(m),

    'select way left': Key('cmd-shift-left'),
    'select way right': Key('cmd-shift-right'),
    'select way up': Key('cmd-shift-up'),
    'select way down': Key('cmd-shift-down'),

    # deleting
    'clear line': Key('cmd-left cmd-left cmd-shift-right delete cmd-right'),

    'clear left': Key('backspace'),
    'clear right': Key('delete'),
    'clear up':  Key('shift-up delete'),
    'clear down':  Key('shift-down delete'),

    'clear word left': Key('alt-backspace'),
    'clear word right': Key('alt-delete'),

    'clear way left': Key('cmd-shift-left delete'),
    'clear way right': Key('cmd-shift-right delete'),
    'clear way up': Key('cmd-shift-up delete'),
    'clear way down': Key('cmd-shift-down delete'),
})
