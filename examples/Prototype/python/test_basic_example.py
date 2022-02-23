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


class TestConcreteClient:
    @pytest.mark.parametrize(
        ('prototype', 'expected'),
        (
            (
                CommonShape(name='test_common', width=1, height=2), dict(name='test_common', width=1, height=2),
                UserDefinedShape(name='test_user_defined', width=3, height=4), dict(name='test_user_defined', width=3, height=4),
            )
        )
    )
    def test_simple_function(self, prototype, expected):
        client = ConcreteClient()
        ret = client.simple_function(prototype)
        assert ret == expected
