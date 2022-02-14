from dataclasses import dataclass
from typing import Sequence


@dataclass
class MenuItem:
    name: str
    price: int
    score: int


class Facade:
    def order_best(self) -> bool:
        all_menu_items: Sequence[MenuItem] = MenuService().get_all_menus()
        print(f'Total {len(all_menu_items)} exists.')

        best_menu: MenuItem = MenuService().get_best_menu()
        print(f'Got best_menu {best_menu}.')

        ordered: bool = OrderService().order(best_menu)
        return ordered


class MenuService:
    MENUS = (
        MenuItem(
            name='Chicken',
            price='18000',
            score=4,
        ),
        MenuItem(
            name='Pizza',
            price='25000',
            score=5,
        ),
        MenuItem(
            name='Salad',
            price='12000',
            score=1,
        ),
    )

    def get_all_menus(self) -> Sequence[MenuItem]:
        return self.MENUS

    def get_best_menu(self) -> Sequence[MenuItem]:
        return sorted(self.MENUS, key=lambda item: item.score, reverse=True)[0]


class OrderService:
    def order(self, menu_item: MenuItem) -> bool:
        print(f'Ordered {menu_item}!')
        return True
