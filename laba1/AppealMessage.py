import datetime

from laba1.Image import Image


class AppealMessage:
    """Класс Сообщения в чате с поддержкой"""
    def __init__(self, text:str, images: list[Image]=None):
        """
        Инициализация сообщения в чате с поддержкой

        Args:
            text: текст сообщения
            images: изображения в сообщении
        """
        self._created_at: datetime.datetime = datetime.datetime.now()
        self._text:str = text

        if images is None:
            self._images = []
        else:
            self._images = images

    def get_created_at(self) -> datetime.datetime:
        return self._created_at

    def set_created_at(self, created_at: datetime.datetime) -> None:
        self._created_at = created_at

    def get_text(self) -> str:
        return self._text

    def set_text(self, text: str) -> None:
        self._text = text

    def get_images(self) -> list[Image]:
        return self._images

    def set_images(self, images: list[Image]) -> None:
        self._images = images

    def add_image(self, image: Image) -> None:
        self._images.append(image)