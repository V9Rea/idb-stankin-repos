from laba1.PaymentMethod import PaymentMethod
from laba1.Profile import Profile
from laba1.account import Account
import re


def create_profile() -> Profile:
    name_pattern = r"[A-Za-zА-яа-я]+"
    phone_pattern = r"[1-9] [0-9]{3} [0-9]{3}-[0-9]{2}-[0-9]{2}"
    email_pattern = r"[A-Za-z0-9.]{1,15}@[A-Za-z]{1,10}.[A-Za-z]{1,10}"
    print("--Создание профиля--")
    while True:
        name = input("Введите имя (одно слово кириллицей или латиницей): ")
        if not re.match(name_pattern, name):
            print("введите корректное имя!")
            continue
        break

    while True:
        surname = input("Введите фамилие (одно слово кириллицей или латиницей): ")
        if not re.match(name_pattern, surname):
            print("введите корректное фамилие!")
            continue
        break

    while True:
        phone = input("Введите телефон (в формате 7 xxx xxx-xx-xx): ")
        if not re.match(phone_pattern, phone):
            print("введите корректный телефон!")
            continue
        break

    while True:
        email = input("Введите email: ")
        if not re.match(email_pattern, email):
            print("введите корректный email!")
            continue
        break

    password = input("Введите пароль: ")

    profile_name = name+'_'+surname

    return Profile(profile_name, email, phone, password)

def create_payment_method() -> PaymentMethod:
    card_number_pattern = r"[0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}"
    expire_date_pattern = r"[0-9][0-9]/[0-9][0-9]"
    cvv_pattern = r"[0-9]{3}"

    print("--Добавление способа оплаты--")
    while True:
        card_num = input("Введите номер карты: ")
        if not re.match(card_number_pattern, card_num):
            print("введите корректный номер карты!")
            continue
        break

    while True:
        expire_date = input("Введите срок действия: ")
        if not re.match(expire_date_pattern, expire_date):
            print("введите корректный срок действия!")
            continue
        break

    while True:
        cvv = input("Введите cvv: ")
        if not re.match(cvv_pattern, cvv):
            print("введите корректный cvv!")
            continue
        break

    email = input("Введите имя на карте: ")

    return PaymentMethod(card_num, expire_date, int(cvv), email)

def create_payment_methods() -> list[PaymentMethod]:
    payment_methods = []

    while True:
        print("Желаете добавить способ оплаты?\n1. Да\n2. Нет")
        try:
            choose = int(input())
        except ValueError:
            print("Введите номер пункта!")
            continue

        if choose == 1:
            payment_methods.append(create_payment_method())
        elif choose == 2:
            break
        else:
            print("Введите корректный номер пункта!")

    return payment_methods

def create_account() -> Account:
    profile = create_profile()
    payment_methods = create_payment_methods()
    return Account(profile, payment_methods)

def main_menu():
    print("""
-----menu-----
1. Создать аккаунт
2. Просмотреть аккаунты
3. Редактировать аккаунт
4. Просмотреть товары
5. Выйти
--------------
    """)

def see_accounts(accounts: list[Account]):
    for num, account in enumerate(accounts):
        print("------ accounts ------")
        print(f"{num+1}. {account.get_profile().get_name()}")
    print("----------------------")

def main():
    accounts: list[Account] = []
    while True:
        main_menu()
        try:
            choose = int(input("Введите номер пункта: "))
        except ValueError:
            print("Введите номер пункта!")
            continue
        if choose == 0:
            break
        if choose == 1:
            accounts.append(create_account())
        if choose == 2:
            see_accounts(accounts)
        if choose == 3:
            see_accounts(accounts)


if __name__ == '__main__':
    main()