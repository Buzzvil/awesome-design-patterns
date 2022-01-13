from dataclasses import dataclass
from typing import Sequence


@dataclass
class MenuItem:
    name: str
    price: int
    score: int


class Facade:
    def order_best(self) -> bool:
        menu_items: Sequence[MenuItem] = MenuService().get_all_menus()
        menu_items.sort(lambda item: item.amount)
        best_menu: MenuItem = menu_items[0]
        ordered: bool = OrderService().order(best_menu)
        return ordered


class MenuService:
    def get_all_menus(self):
        pass


class OrderService:
    def order(self, menu_item: MenuItem):
        pass
