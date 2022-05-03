from examples.Visitor.visitor_example import App, Beverage, Snack, CompositeProduct, ConcreteVisitor


def test_visitor():
    app = App()
    products = [Beverage(), Snack(), Snack()]
    composite = CompositeProduct()
    for product in products:
        composite.add(product)
    visitor = ConcreteVisitor()
    assert app.main(p=composite, v=visitor) == 1500 + 2000 + 2000
