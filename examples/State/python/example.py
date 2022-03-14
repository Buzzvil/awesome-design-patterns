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
        if c == 'h':
            editor.pos_x = max(0, editor.pos_x - 1)
        elif c == 'j':
            editor.pos_y = max(0, editor.pos_y - 1)
        elif c == 'k':
            editor.pos_y += min(len(editor.text), editor.pos_y + 1)
        elif c == 'l':
            editor.pos_x += min(len(editor.text[editor.pos_y]), editor.pos_x + 1)
        elif c == 'x':
            editor.text[editor.pos_y].pop(editor.pos_x - 1)
            if editor.pos_x >= len(editor.text[editor.pos_y]):
                editor.pos_x -= 1
        elif c == 'i':
            editor.mode = InsertMode()
        elif c == 'v':
            editor.mode = VisualMode()


class InsertMode(Mode):
    def process_input(self, editor: Editor, c: Optional[str]) -> None:
        if c == ESCAPE_CHARACTER:
            editor.mode = NormalMode()
        else:
            if editor.pos_y > len(editor.text):
                editor.text.append(list())
            editor.text[editor.pos_y].insert(editor.pos_x, c)
            editor.pos_x += 1


class VisualMode(Mode):
    def __init__(self):
        super(VisualMode, self).__init__()
        self._new_x = -1
        self._new_y = -1

    def process_input(self, editor: Editor, c: Optional[str]) -> None:
        if c == ESCAPE_CHARACTER:
            editor.mode = NormalMode()
        if self._new_x == -1:
            self._new_x = editor.pos_x
            self._new_y = editor.pos_y
        if c == 'h':
            self._new_x = max(0, self._new_x - 1)
        elif c == 'j':
            self._new_y = min(len(editor.text), self._new_y + 1)
        elif c == 'k':
            self._new_y = max(0, self._new_y - 1)
        elif c == 'l':
            self._new_y = min(len(editor.text[self._new_x]), self._new_x + 1)
        elif c == 'x':
            for y in range(min(editor.pos_y, self._new_y), max(editor.pos_y, self._new_y) + 1):
                min_x = min(editor.pos_x, self._new_x)
                max_x = max(editor.pos_x, self._new_x)
                editor.text[y] = editor.text[y][:min_x] + editor.text[y][max_x + 1:]
