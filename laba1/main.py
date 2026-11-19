from laba1.Image import Image
from laba1.PaymentMethod import PaymentMethod
from laba1.Product import Product
from laba1.ProductParam import ProductParam
from laba1.Profile import Profile
from laba1.account import Account
from laba1.description import Description
import json
import os
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

def create_product_param() -> ProductParam:
    print("--Добавление параметра товара--")
    while True:
        name = input("Введите название параметра: ")
        if name == "":
            print("введите корректное название!")
            continue
        break

    while True:
        value = input("Введите значение параметра: ")
        if value == "":
            print("введите корректное значение!")
            continue
        break

    return ProductParam(name, value)

def create_product_params() -> list[ProductParam]:
    product_params = []

    while True:
        print("Желаете добавить параметр товара?\n1. Да\n2. Нет")
        try:
            choose = int(input())
        except ValueError:
            print("Введите номер пункта!")
            continue

        if choose == 1:
            product_params.append(create_product_param())
        elif choose == 2:
            break
        else:
            print("Введите корректный номер пункта!")

    return product_params

def create_description() -> Description:
    print("--Добавление описания--")
    while True:
        image_name = input("Введите название изображения: ")
        if image_name == "":
            print("введите корректное название!")
            continue
        break

    while True:
        image_content = input("Введите содержимое изображения: ")
        if image_content == "":
            print("введите корректное содержимое!")
            continue
        break

    while True:
        text = input("Введите текст описания: ")
        if text == "":
            print("введите корректное описание!")
            continue
        break

    return Description(Image(image_name, image_content), text)

def create_product() -> Product:
    print("--Добавление товара--")
    while True:
        name = input("Введите название товара: ")
        if name == "":
            print("введите корректное название!")
            continue
        break

    while True:
        try:
            price = float(input("Введите цену: "))
        except ValueError:
            print("введите корректную цену!")
            continue
        if price < 0:
            print("введите корректную цену!")
            continue
        break

    description = create_description()
    product_params = create_product_params()
    return Product(name, price, description, product_params, [])

def main_menu():
    print("""
-----menu-----
1. Создать аккаунт
2. Просмотреть аккаунты
3. Редактировать аккаунт
4. Добавить товар
5. Просмотреть товары
6. Выйти
--------------
    """)

def see_accounts(accounts: list[Account]):
    if len(accounts) == 0:
        print("Аккаунтов нет!")
        return

    print("------ accounts ------")
    for num, account in enumerate(accounts):
        print(f"{num+1}. {account.get_profile().get_name()}")
    print("----------------------")

def see_products(products: list[Product]):
    if len(products) == 0:
        print("Товаров нет!")
        return

    for num, product in enumerate(products):
        print("------ products ------")
        print(f"{num+1}. {product.get_name()}")
        print(f"Цена: {product.get_price()}")
        print(f"Описание: {product.get_description().get_text()}")
        print(f"Изображение: {product.get_description().get_image().get_name()}")
        for param in product.get_product_params():
            print(f"{param.get_name()}: {param.get_value()}")
    print("----------------------")

def see_payment_methods(payment_methods: list[PaymentMethod]):
    if payment_methods is None or len(payment_methods) == 0:
        print("Способов оплаты нет!")
        return

    print("------ payment methods ------")
    for num, method in enumerate(payment_methods):
        print(f"{num+1}. {method.get_owner_name()} {method.get_card_number()} {method.get_expiry_date()}")
    print("----------------------")

def edit_profile_name(profile: Profile):
    name_pattern = r"[A-Za-zА-яа-я]+"
    print("--Изменение имени--")

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

    profile.set_name(name+'_'+surname)

def edit_profile_phone(profile: Profile):
    phone_pattern = r"[1-9] [0-9]{3} [0-9]{3}-[0-9]{2}-[0-9]{2}"
    print("--Изменение телефона--")
    while True:
        phone = input("Введите телефон (в формате 7 xxx xxx-xx-xx): ")
        if not re.match(phone_pattern, phone):
            print("введите корректный телефон!")
            continue
        break

    profile.set_phone(phone)

def edit_profile_email(profile: Profile):
    email_pattern = r"[A-Za-z0-9.]{1,15}@[A-Za-z]{1,10}.[A-Za-z]{1,10}"
    print("--Изменение email--")
    while True:
        email = input("Введите email: ")
        if not re.match(email_pattern, email):
            print("введите корректный email!")
            continue
        break

    profile.set_email(email)

def edit_profile_password(profile: Profile):
    print("--Изменение пароля--")
    password = input("Введите пароль: ")
    profile.set_password(password)

def edit_menu():
    print("""
-----редактирование-----
1. Изменить имя
2. Изменить телефон
3. Изменить email
4. Изменить пароль
5. Добавить способ оплаты
6. Просмотреть способы оплаты
7. Назад
--------------
    """)

def edit_account(accounts: list[Account]):
    if len(accounts) == 0:
        print("Аккаунтов нет!")
        return

    see_accounts(accounts)
    while True:
        try:
            choose = int(input("Введите номер аккаунта: "))
        except ValueError:
            print("Введите номер пункта!")
            continue

        if choose < 1 or choose > len(accounts):
            print("Введите корректный номер пункта!")
            continue
        break

    account = accounts[choose - 1]
    print("--Вход в аккаунт--")
    email = input("Введите email: ")
    password = input("Введите пароль: ")
    profile = account.get_profile()
    if email != profile.get_email() or password != profile.get_password():
        print("Неверный email или пароль!")
        return

    while True:
        edit_menu()
        try:
            action = int(input("Введите номер пункта: "))
        except ValueError:
            print("Введите номер пункта!")
            continue

        if action == 7:
            break
        elif action == 1:
            edit_profile_name(profile)
        elif action == 2:
            edit_profile_phone(profile)
        elif action == 3:
            edit_profile_email(profile)
        elif action == 4:
            edit_profile_password(profile)
        elif action == 5:
            for method in create_payment_methods():
                account.add_payment_methods(method)
        elif action == 6:
            see_payment_methods(account.get_payment_methods())
        else:
            print("Введите корректный номер пункта!")

def create_accounts_from_data(accounts_data: list) -> list[Account]:
    accounts = []
    for account_data in accounts_data:
        profile_data = account_data["profile"]
        profile = Profile(profile_data["name"], profile_data["email"], profile_data["phone"], profile_data["password"])
        payment_methods = []
        for method_data in account_data["payment_methods"]:
            payment_methods.append(PaymentMethod(
                method_data["card_number"],
                method_data["expiry_date"],
                int(method_data["cvv"]),
                method_data["owner_name"]
            ))
        accounts.append(Account(profile, payment_methods))
    return accounts

def create_products_from_data(products_data: list) -> list[Product]:
    products = []
    for product_data in products_data:
        image_data = product_data["description"]["image"]
        description = Description(Image(image_data["name"], image_data["content"]), product_data["description"]["text"])
        product_params = []
        for param_data in product_data["product_params"]:
            product_params.append(ProductParam(param_data["name"], param_data["value"]))
        products.append(Product(product_data["name"], float(product_data["price"]), description, product_params, []))
    return products

def load_test_data() -> tuple[list[Account], list[Product]]:
    data_path = os.path.join(os.path.dirname(__file__), "test_data.json")
    with open(data_path, encoding="utf-8") as file:
        data = json.load(file)
    return create_accounts_from_data(data["accounts"]), create_products_from_data(data["products"])

def main():
    accounts, products = load_test_data()
    while True:
        main_menu()
        try:
            choose = int(input("Введите номер пункта: "))
        except ValueError:
            print("Введите номер пункта!")
            continue
        if choose == 6:
            break
        elif choose == 1:
            accounts.append(create_account())
        elif choose == 2:
            see_accounts(accounts)
        elif choose == 3:
            edit_account(accounts)
        elif choose == 4:
            products.append(create_product())
        elif choose == 5:
            see_products(products)
        else:
            print("Введите корректный номер пункта!")


if __name__ == '__main__':
    main()