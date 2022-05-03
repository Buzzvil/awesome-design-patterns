import pytest

from examples.Prototype.python.basic_example import CommonShape, UserDefinedShape, ConcreteClient, PickyClient


class TestShape:
    @pytest.mark.parametrize('shape', (CommonShape(), UserDefinedShape()))
    def test_clone(self, shape):
        shape.name = 'test_common'
        shape.width = 1
        shape.height = 2

        clone = shape.clone()
        assert clone.name == shape.name
        assert clone.width == shape.width
        assert clone.height == shape.height


class TestClient:
    @pytest.mark.parametrize(
        ('client', 'shape_cls', 'shape_kwargs', 'expected'),
        (
            (
                ConcreteClient(),
                CommonShape,
                dict(name='test_common', width=1, height=2),
                dict(name='test_common', width=1, height=2),
            ),
            (
                PickyClient(),
                UserDefinedShape,
                dict(name='test_user_defined', width=3, height=4, memo='test_memo'),
                dict(name='test_user_defined', width=3, height=4, memo='new_memo'),
            )
        )
    )
    def test_simple_function(self, client, shape_cls, shape_kwargs, expected):
        shape = shape_cls()
        for k, v in shape_kwargs.items():
            setattr(shape, k, v)
        ret = client.simple_function(shape)
        assert ret == expected
