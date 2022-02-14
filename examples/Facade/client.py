from typing import Sequence

from subsystem import MenuService, MenuItem, OrderService, Facade


class SubSystemAwareClient:
    def order_best(self) -> bool:
        all_menu_items: Sequence[MenuItem] = MenuService().get_all_menus()
        print(f'Total {len(all_menu_items)} exists.')

        best_menu: MenuItem = MenuService().get_best_menu()
        print(f'Got best_menu {best_menu}.')

        ordered: bool = OrderService().order(best_menu)
        return ordered


class Client:
    def order_best(self) -> bool:
        facade = Facade()
        return facade.order_best()


if __name__ == '__main__':
    client = Client()
    client.order_best()
    # >> Total 3 exists.
    # >> Got best_menu MenuItem(name='Pizza', price='25000', score=5).
    # >> Ordered MenuItem(name='Pizza', price='25000', score=5)!
