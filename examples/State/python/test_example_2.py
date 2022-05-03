import pytest

from examples.State.python.example_2 import Editor, InsertMode, NormalMode, VisualMode


@pytest.mark.parametrize(
    ('inputs', 'expected_text', 'expected_position', 'expected_mode'),
    (
        ('iabcd', [['a', 'b', 'c', 'd']], [4, 0], InsertMode),
        ('iabcd^xxx', [['a']], [1, 0], NormalMode),
        ('iabcd^hhix', [['a', 'b', 'x', 'c', 'd']], [3, 0], InsertMode),
        ('iabcd^ox', [['a', 'b', 'c', 'd'], ['x']], [1, 1], InsertMode),
        ('iabcd^oefgh^oijkl^vk', [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l']], [4, 1], VisualMode),
        ('iabcd^oefgh^oijkl^vkx', [['a', 'b', 'c', 'd'], ['e', 'f', 'g'], ['i', 'j', 'k']], [3, 1], NormalMode),
    )
)
def test_editor(inputs, expected_text, expected_position, expected_mode):
    editor = Editor()
    for c in inputs:
        editor.process_input(c)
    assert editor.text == expected_text
    assert editor.pos_x == expected_position[0]
    assert editor.pos_y == expected_position[1]
    assert isinstance(editor.mode, expected_mode)
