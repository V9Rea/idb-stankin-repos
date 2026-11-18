import datetime

from laba1.Image import Image


class AppealMessage:
    def __init__(self, created_at: datetime.datetime, text:str, images: list[Image]):
        self._created_at: datetime.datetime = created_at
        self._text:str = text
        self._images: list[Image] = images

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