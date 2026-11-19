class ProductParam:
    """Класс параметра товара"""
    def __init__(self, name:str, value:str):
        """
        Инициализирует объект описания

        Args:
            name: имя параметра
            value: значение параметра
        """
        self.name:str = name
        self.value:str = value

    def get_name(self) -> str:
        return self.name

    def set_name(self, name:str):
        self.name = name

    def get_value(self) -> str:
        return self.value

    def set_value(self, value: str):
        self.value = value