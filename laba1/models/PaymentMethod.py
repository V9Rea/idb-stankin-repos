import datetime


class PaymentMethod:
    """Класс способа оплаты"""
    def __init__(self, card_number: str, expiry_date: str, cvv: int, owner_name: str):
        """
        Инициализирует объект описания

        Args:
            card_number: номер карты
            expiry_date: срок действия
            cvv: код
            owner_name: имя владельца
        """
        self._card_number: str = card_number
        self._expiry_date: str = expiry_date
        self._cvv: int = cvv
        self._owner_name: str = owner_name

    def get_card_number(self) -> str:\
        return self._card_number

    def set_card_number(self, card_number: str) -> None:
        self._card_number = card_number

    def get_expiry_date(self) -> str:
        return self._expiry_date

    def set_expiry_date(self, expiry_date: str) -> None:
        self._expiry_date = expiry_date

    def get_cvv(self) -> int:
        return self._cvv

    def set_cvv(self, cvv: int) -> None:
        self._cvv = cvv

    def get_owner_name(self) -> str:
        return self._owner_name
