# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Document(ABC):
    def open(self):
        print('Open Document')

    def save(self):
        print('Save Document')

    def close(self):
        print('Close Document')


class DrawingDocument(Document):
    def open(self):
        print('Open drawing document')


class TextDocument(Document):
    def open(self):
        print('Open text document')


class Application(ABC):
    @abstractmethod
    def create_document(self) -> Document:
        raise NotImplementedError()

    def new_document(self):
        document = self.create_document()
        document.open()


class DrawingApplication(Application):
    def create_document(self) -> Document:
        return DrawingDocument()


class TextApplication(Application):
    def create_document(self) -> Document:
        return TextDocument()


if __name__ == "__main__":
    DrawingApplication().new_document()
    # open drawing document

    TextApplication().new_document()
    # Open text document
