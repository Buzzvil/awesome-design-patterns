from typing import Sequence

from examples.Facade.subsystem import MenuService, MenuItem, OrderService, Facade


class SubSystemAwareClient:
    def order_best(self) -> bool:
        menu_items: Sequence[MenuItem] = MenuService().get_all_menus()
        menu_items.sort(lambda item: item.amount)
        best_menu: MenuItem = menu_items[0]
        ordered: bool = OrderService().order(best_menu)
        return ordered


class Client:
    def order_best(self) -> bool:
        facade = Facade()
        return facade.order_best()
