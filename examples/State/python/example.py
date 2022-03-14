from abc import abstractmethod, ABC
from typing import Optional, List

ESCAPE_CHARACTER = '^'


class Editor:
    def __init__(self) -> None:
        self.text: List[List[str]] = [[]]
        self.pos_x: int = 0
        self.pos_y: int = 0
        self.mode: Mode = NormalMode()

    def process_input(self, c: str) -> None:
        self.mode.process_input(self, c)


class Mode(ABC):
    @abstractmethod
    def process_input(self, editor: Editor, c: Optional[str]) -> None:
        pass


class NormalMode(Mode):
    def process_input(self, editor: Editor, c: Optional[str]) -> None:
        if c == 'h':  # move left
            editor.pos_x = max(0, editor.pos_x - 1)
        elif c == 'j':  # move down
            editor.pos_y += min(len(editor.text), editor.pos_y + 1)
        elif c == 'k':  # move up
            editor.pos_y = max(0, editor.pos_y - 1)
        elif c == 'l':  # move right
            editor.pos_x += min(len(editor.text[editor.pos_y]), editor.pos_x + 1)
        elif c == 'x':  # delete character at current position
            editor.text[editor.pos_y].pop(editor.pos_x - 1)
            if editor.pos_x >= len(editor.text[editor.pos_y]):
                editor.pos_x -= 1
        elif c == 'o':  # add new line and start insert
            editor.pos_y += 1
            editor.pos_x = 0
            editor.text.insert(editor.pos_y, list())
            editor.mode = InsertMode()
        elif c == 'i':  # start insert
            editor.mode = InsertMode()
        elif c == 'v':  # start visual mode
            editor.mode = VisualMode()


class InsertMode(Mode):
    def process_input(self, editor: Editor, c: Optional[str]) -> None:
        if c == ESCAPE_CHARACTER:  # stop insert mode
            editor.mode = NormalMode()
        else:
            if editor.pos_y > len(editor.text):
                editor.text.append(list())
            editor.text[editor.pos_y].insert(editor.pos_x, c)
            editor.pos_x += 1


class VisualMode(Mode):
    def __init__(self):
        super(VisualMode, self).__init__()
        self._orig_x = -1
        self._orig_y = -1

    def process_input(self, editor: Editor, c: Optional[str]) -> None:
        if c == ESCAPE_CHARACTER:
            editor.mode = NormalMode()
        if self._orig_x == -1:
            self._orig_x = editor.pos_x
            self._orig_y = editor.pos_y
        if c == 'h':  # move left
            editor.pos_x = max(0, editor.pos_x - 1)
        elif c == 'j':  # move down
            editor.pos_y += min(len(editor.text), editor.pos_y + 1)
        elif c == 'k':  # move up
            editor.pos_y = max(0, editor.pos_y - 1)
        elif c == 'l':  # move right
            editor.pos_x += min(len(editor.text[editor.pos_y]), editor.pos_x + 1)
        elif c == 'x':  # delete all characters in scope
            for y in range(min(editor.pos_y, self._orig_y), min(max(editor.pos_y, self._orig_y) + 1, len(editor.text))):
                min_x = min(editor.pos_x, self._orig_x)
                max_x = max(editor.pos_x, self._orig_x)
                editor.text[y] = editor.text[y][:min_x - 1] + editor.text[y][min(max_x, len(editor.text[y])):]
            editor.pos_x -= 1
            editor.mode = NormalMode()
