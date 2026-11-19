import datetime

from laba1.Product import Product


class Order:
    """Класс заказа"""
    def __init__(self, created_at: datetime.datetime, pickup_date: datetime.datetime, price: float, products: list[Product], status: str) -> None:
        """
        Инициализирует объект pfrfpf

        Args:
            created_at: дата создания
            pickup_date: дата получения
            price: цена
            products: товары
            status: статус заказа
        """
        self._created_at: datetime.datetime = created_at
        self._pickup_date: datetime.datetime = pickup_date
        self._price: float = price
        self._products: list[Product] = products
        self._status: str = status


    def get_created_at(self) -> datetime.datetime:
        return self._created_at

    def get_pickup_date(self) -> datetime.datetime:
        return self._pickup_date

    def set_pickup_date(self, pickup_date: datetime.datetime) -> None:
        self._pickup_date = pickup_date

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
        self._price = price

    def get_products(self) -> list[Product]:
        return self._products

    def add_products(self, products: Product) -> None:
        self._products.append(products)

    def get_status(self) -> str:
        return self._status

    def set_status(self, status: str) -> None:
        self._status = status


