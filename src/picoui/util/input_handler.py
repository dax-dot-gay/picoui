from enum import StrEnum
import string
from typing import Generator

from readchar import readkey, key


class Keys(StrEnum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    ENTER = "enter"
    ESCAPE = "escape"
    HOME = "home"
    END = "end"
    PAGE_UP = "page_up"
    PAGE_DOWN = "page_down"
    INSERT = "insert"
    DELETE = "delete"
    BACKSPACE = "backspace"
    TAB = "tab"


def parse_read_key(current: str) -> Keys | str | None:
    match current:
        case key.UP:
            return Keys.UP
        case key.DOWN:
            return Keys.DOWN
        case key.LEFT:
            return Keys.LEFT
        case key.RIGHT:
            return Keys.RIGHT
        case key.ENTER:
            return Keys.ENTER
        case key.ESC:
            return Keys.ESCAPE
        case key.HOME:
            return Keys.HOME
        case key.END:
            return Keys.END
        case key.PAGE_UP:
            return Keys.PAGE_UP
        case key.PAGE_DOWN:
            return Keys.PAGE_DOWN
        case key.INSERT:
            return Keys.INSERT
        case key.DELETE:
            return Keys.DELETE
        case key.BACKSPACE:
            return Keys.BACKSPACE
        case key.TAB:
            return Keys.TAB
        case _:
            if current == key.ESC + key.ESC:
                return Keys.ESCAPE
            if current in string.printable:
                return current

    return None


def keys() -> Generator[Keys | str, None, None]:
    while True:
        read = parse_read_key(readkey())
        if read:
            yield read
