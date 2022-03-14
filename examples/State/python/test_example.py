import pytest

from examples.State.python.example import Editor


@pytest.mark.parametrize(
    ('inputs', 'expected_text', 'expected_position'),
    (
        ('iabcdefg', [['a', 'b', 'c', 'd', 'e', 'f', 'g']], [7, 0]),
        ('iabcdefg^xxx', [['a', 'b', 'c', 'd']], [4, 0]),
    )
)
def test_editor(inputs, expected_text, expected_position):
    editor = Editor()
    for c in inputs:
        editor.process_input(c)
    assert editor.text == expected_text
    assert editor.pos_x == expected_position[0]
    assert editor.pos_y == expected_position[1]
