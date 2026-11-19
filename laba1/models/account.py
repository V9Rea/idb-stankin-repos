from laba1.models.Order import Order
from laba1.models.PaymentMethod import PaymentMethod
from laba1.models.Product import Product
from laba1.models.Profile import Profile
from laba1.models.Review import Review
from laba1.models.ServiceAppeal import ServiceAppeal


class Account:
    """Класс аккаунта пользователя"""

    def __init__(self, profile: Profile, payment_methods: list[PaymentMethod]=None) -> None:
        """
        Инициализация объекта аккаунта

        Args:
            profile: профиль пользователя
            payment_methods: способы оплаты
        """

        self._profile: Profile = profile
        self._favourites: list[Product] = []
        self._basket : list[Product] = []
        self._orders: list[Order] = []
        self._reviews: list[Review] = []
        self._service_appeals: list[ServiceAppeal] = []

        if payment_methods is None:
            self._payment_methods: list[PaymentMethod] = []
        else:
            self._payment_methods: list[PaymentMethod] = payment_methods

    def get_profile(self) -> Profile:
        return self._profile

    def set_profile(self, profile: Profile) -> None:
        self._profile = profile

    def get_favourites(self) -> list[Product]:
        return self._favourites

    def add_favourites(self, favourites: Product) -> None:
        self._favourites.append(favourites)

    def get_payment_methods(self) -> list[PaymentMethod]:
        return self._payment_methods

    def add_payment_methods(self, payment_methods: PaymentMethod) -> None:
        self._payment_methods.append(payment_methods)

    def get_basket(self) -> list[Product]:
        return self._basket

    def add_basket(self, product: Product) -> None:
        self._basket.append(product)

    def get_orders(self) -> list[Order]:
        return self._orders

    def add_orders(self, orders: Order) -> None:
        self._orders.append(orders)

    def get_reviews(self) -> list[Review]:
        return self._reviews

    def add_reviews(self, reviews: Review) -> None:
        self._reviews.append(reviews)

    def get_service_appeals(self) -> list[ServiceAppeal]:
        return self._service_appeals

    def add_service_appeals(self, service_appeals: ServiceAppeal) -> None:
        self._service_appeals.append(service_appeals)

