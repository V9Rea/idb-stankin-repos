class ProductParam:
    def __init__(self, name:str, value:str):
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