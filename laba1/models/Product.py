from laba1.models.ProductParam import ProductParam
from laba1.models.Review import Review
from laba1.models.description import Description


class Product:
    """Класс товара"""
    def __init__(self, name: str, price: float, description: Description, product_params:list[ProductParam], review : list[Review]) -> None:
        """
        Инициализирует объект класса товар

        Args:
            name: изображение
            price: текст описания
            description: описание товара
            product_params: параметры товара
            review: отзывы на товар
        """
        self._name: str = name
        self._price: float = price
        self._description: Description = description
        self._product_params:list[ProductParam] = product_params
        self._review : list[Review] = review

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name
    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
       self._price = price

    def get_description(self) -> Description:
        return self._description

    def set_description(self, description: Description) -> None:
        self._description = description

    def get_product_params(self) -> list[ProductParam]:
        return self._product_params

    def add_product_params(self, product_params: ProductParam) -> None:
        self._product_params.append(product_params)

    def get_review(self) -> list[Review]:
        return self._review

    def set_review(self, review: Review) -> None:
        self._review.append(review)
