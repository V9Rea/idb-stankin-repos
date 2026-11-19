import datetime

from laba1.models.AppealMessage import AppealMessage


class ServiceAppeal:
    """Класс чата сервисной поддержки"""
    def __init__(self):
        """
        Инициализирует объект чата сервисной поддержки
        """

        self._created_at: datetime.datetime = datetime.datetime.now()
        self._appeal_message: list[AppealMessage] = []

    def get_created_at(self) -> datetime.datetime:
        return self._created_at

    def add_appeal_message(self, appeal_message: AppealMessage):
        self._appeal_message.append(appeal_message)

    def get_appeal_messages(self) -> list[AppealMessage]:
        return self._appeal_message

