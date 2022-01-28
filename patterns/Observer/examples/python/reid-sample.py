from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Article(object):
    title: str
    category: str
    link: str

    def __init__(self, title: str, category: str, link: str):
        self.title = title
        self.category = category
        self.link = link


class SubscribeManager(ABC):
    @abstractmethod
    def subscribe(self, observer: ArticleObserver) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: ArticleObserver) -> None:
        pass

    @abstractmethod
    def notify(self, article: Article) -> None:
        pass


class BlogService(SubscribeManager):
    _articles: List[Article] = []
    _observers: List[ArticleObserver] = []

    def subscribe(self, observer: ArticleObserver) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: ArticleObserver) -> None:
        self._observers.remove(observer)

    def notify(self, article: Article) -> None:
        for observer in self._observers:
            observer.update(article)

    def posting(self, article: Article):
        self.notify(article)


class ArticleObserver(ABC):
    @abstractmethod
    def update(self, article: Article) -> None:
        pass


class AnimalArticleObserver(ArticleObserver):
    def update(self, article: Article) -> None:
        if 'Animal' in article.category:
            print('Animal Article Uploaded : {}\ncategory: {}\nlink : {}\n'.format(article.title, article.category, article.link))


class FoodArticleObserver(ArticleObserver):
    def update(self, article: Article) -> None:
        if 'Food' in article.category:
            print('Food Article Uploaded : {}\ncategory: {}\nlink : {}\n'.format(article.title, article.category, article.link))


class ITArticleObserver(ArticleObserver):
    def update(self, article: Article) -> None:
        if 'IT' in article.category:
            print('IT Article Uploaded : {}\ncategory: {}\nlink : {}\n'.format(article.title, article.category, article.link))


if __name__ == "__main__":
    blog_service = BlogService()
    blog_service.subscribe(AnimalArticleObserver())
    blog_service.subscribe(FoodArticleObserver())
    blog_service.subscribe(ITArticleObserver())

    article = Article(
        title='My cat is typing my Computer',
        category='IT/Animal',
        link='https://www.sampleblog.co.kr/posting/1',
    )
    blog_service.posting(article)

    article = Article(
        title='I like Korean food',
        category='Food',
        link='https://www.sampleblog.co.kr/posting/3',
    )
    blog_service.posting(article)
