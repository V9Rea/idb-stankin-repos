from laba1.Image import Image


class Description:
    """Класс описания """
    def __init__(self, image: Image, text: str):
        """
        Инициализирует объект описания

        Args:
            image: изображение
            text: текст описания
        """
        self.image: Image = image
        self.text: str = text

    def get_image(self) -> Image:
        return self.image

    def set_image(self, image: Image) -> None:
        self.image = image

    def get_text(self) -> str:
        return self.text

    def set_text(self, text: str) -> None:
        self.text = text



