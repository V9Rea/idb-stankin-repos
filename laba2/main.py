# -((((-1a +3b * ((a - b) - c))*12 - 5) -54) *9)

import re
not_particle = "не "

operand = r"(?:[1-9]+[A-Za-z]|[A-Za-z](?:[1-9][0-9]*)?|[^0-9A-za-z]0[^0-9A-za-z]|[1-9][0-9]*)" # Операнд: число, буква, число+буква (1a) или буква+индекс (a1)

prefix = r"(?:[-+(]\s*)*" # Префикс перед операндом: любые комбинации унарных +/-, открывающих скобок и пробелов

suffix = r"(?:\s*\))*" # Суффикс после операнда: любые комбинации закрывающих скобок и пробелов

operator = r"\s*[-+*/:]\s*" # Бинарный оператор с возможными пробелами вокруг

math_expr_pattern = rf"{prefix}{operand}{suffix}(?:{operator}{prefix}{operand}{suffix})+" # Полный паттерн: минимум одна операция или скобки, чтобы не ловить обычные слова/числа

def check_bracket(string: str) -> bool:
    stack = []

    if string.count("(") == 0 and string.count(")") == 0:
        return True

    if string.count("(") != string.count(")"):
        return False

    for char in string:
        if char == "(":
            stack.append(char)
        if char == ")":
            stack.pop()
    if len(stack) == 0:
        return True
    return False


def search_math_line_in_file(filepath: str) -> list[str]|None:
    try:
        file = open(filepath, "r", encoding="utf-8")
    except FileNotFoundError:
        return None
    math_lines = re.findall(math_expr_pattern, file.read())

    return math_lines

def file_input():
    line = input("Введите путь к файлу: ")
    if search_math_line_in_file(line) is None:
        print("Неправильный путь к файлу!")


def check_string(string: str) -> bool:
    match = re.match(math_expr_pattern, string)
    if match and check_bracket(string):
        return True
    return False

def user_input() -> str:
    option = input("Введите математическое выражение: ")
    return option

def menu():
    print("""
--------- меню ---------
1. Ручной ввод
2. Ввод из файла
3. Выход
------------------------
""")

def manual_input():
    line = user_input()
    particle = not_particle
    if check_string(line):
        particle = ""
    print(f"Строка \"{line}\" {particle}является математическим выражением")

def main():
    menu()
    while True:
        try:
            choose = int(input("Введите номер пункта: "))
        except ValueError:
            print("Введите корректный номер!")
            continue

        if choose == 1:
            user_input()
            continue
        if choose == 2:
            file_input()
            continue
        if choose == 3:
            break
        else:
            print("Введите корректный пункт!")


if __name__ == '__main__':
    main()