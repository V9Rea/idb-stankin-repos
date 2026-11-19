class Image:
    """Класс изображения"""
    def __init__(self, name: str, content: str):
        """
        Инициализирует объект описания

        Args:
            name: имя изображения
            content: содержание изображения
        """
        self._name: str = name
        self._content: str = content

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_content(self) -> str:
        return self._content

    def set_content(self, content: str) -> None:
        self._content = content