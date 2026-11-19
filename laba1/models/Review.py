import datetime


class Review:
    """Класс отзыва"""
    def __init__(self, created_at:datetime.datetime, author_name:str, rate:int, review:str):
        """
        Инициализирует объект отзыва

        Args:
            created_at: дата создания отзыва
            author_name: автор отзыва
            rate: оценка
            review: текст отзыва
        """
        self._created_at:datetime.datetime = created_at
        self._author_name:str = author_name
        self._rate:int = rate
        self._review:str = review

    def set_author_name(self, author_name:str):
        self._author_name:str = author_name

    def get_author_name(self):
        return self._author_name

    def set_rate(self, rate:int):
        self._rate:int = rate

    def get_rate(self):
        return self._rate

    def set_review(self, review:str):
        self._review:str = review

    def get_review(self):
        return self._review

    def get_created_at(self) -> datetime.datetime:
        return self._created_at
