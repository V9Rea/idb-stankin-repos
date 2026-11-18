class Profile:
    def __init__(self, name: str, email: str, phone: str, password: str):
        self._name: str = name
        self._email: str = email
        self._phone: str = phone
        self._password: str = password


    def get_name(self) -> str:
        return self._name

    def set_name(self, name:str):
        self._name = name

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_phone(self) -> str:
        return self._phone

    def set_phone(self, phone: str):
        self._phone = phone

    def get_password(self) -> str:
        return self._password

    def set_password(self, password: str):
        self._password = password
