# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    name: str
    size: int

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    @abstractmethod
    def show(self, path: str = '') -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_size(self) -> int:
        raise NotImplementedError()


class Directory(Component):
    children: List[Component]

    def __init__(self, name: str) -> None:
        super(Directory, self).__init__(name, 0)
        self.children = []

    def show(self, path: str = '') -> None:
        for child in self.children:
            child.show(path + '/' + self.name)

    def add_component(self, component: Component) -> None:
        self.children.append(component)

    def get_size(self) -> int:
        sum_size: int = 0
        for child in self.children:
            sum_size = sum_size + child.get_size()
        return sum_size


class File(Component):
    def show(self, path: str = '') -> None:
        print(path + '/' + self.name)

    def get_size(self) -> int:
        return self.size


if __name__ == "__main__":
    image_png = File('image1.png', 100)
    image_jpg = File('image2.jpg', 200)
    image_directory = Directory('Image')
    image_directory.add_component(image_jpg)
    image_directory.add_component(image_png)

    document_pdf = File('document1.pdf', 300)
    document_xls = File('document2.xls', 400)
    document_doc = File('document3.doc', 500)
    document_directory = Directory('Document')
    document_directory.add_component(document_xls)
    document_directory.add_component(document_xls)
    document_directory.add_component(document_doc)

    game = File('game.exe', 600)
    desktop = Directory('Desktop')
    desktop.add_component(game)
    desktop.add_component(image_directory)
    desktop.add_component(document_directory)

    image_directory.show()
    # /Image/image2.jpg
    # /Image/image1.png

    desktop.show()
    # /Desktop/game.exe
    # /Desktop/Image/image2.jpg
    # /Desktop/Image/image1.png
    # /Desktop/Document/document2.xls
    # /Desktop/Document/document2.xls
    # /Desktop/Document/document3.doc

    print(f'Document directory size : {document_directory.get_size()}')
    # Document directory size : 1300
    print(f'Desktop  directory size : {desktop.get_size()}')
    # Desktop  directory size : 2200
