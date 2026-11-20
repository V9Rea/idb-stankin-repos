import re
not_particle = "не "

operand = r"(?:[1-9]+[A-Za-z]|[A-Za-z](?:[1-9][0-9]*)?|[^0-9A-za-z]0[^0-9A-za-z]|[1-9][0-9]*)" # Операнд: число, буква, число+буква (1a) или буква+индекс (a1)

prefix = r"(?:[-+(]\s*)*" # Префикс перед операндом: любые комбинации  +/-, открывающих скобок и пробелов

suffix = r"(?:\s*\))*" #любые комбинации закрывающих скобок и пробелов

operator = r"\s*[-+*/:]\s*" # Бинарный оператор с возможными пробелами вокруг

math_expr_pattern = rf"(?<![A-Za-z0-9]){prefix}{operand}{suffix}(?:{operator}{prefix}{operand}{suffix})+(?![A-Za-z0-9])" #минимум одна операция или скобки, чтобы не ловить обычные слова/числа


def check_bracket(string: str) -> bool:
    """
    Проверка на корректность расстановки скобок в выражении

    Args:
        string: строка с выбражением
    Returns:
        True/False в зависимости от корректности/некорректности расстановки строк
    """
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
    """
    Поиск в файле математических выражений

    Args:
        filepath: путь к файлу
    Returns:
        list[str] при успешном выполнении и None при ошибках
    """

    try:
        file = open(filepath, "r", encoding="utf-8")
    except FileNotFoundError:
        return None
    math_lines = re.findall(math_expr_pattern, file.read())

    correct_lines = [math_lines for math_lines in math_lines if check_bracket(math_lines)]

    return correct_lines

def file_input():
    line = input("Введите путь к файлу: ")
    if search_math_line_in_file(line) is None:
        print("Неправильный путь к файлу!")


def check_string(string: str) -> bool:
    """
    Поиск математического выражения в строке

    Args:
        string: строка, в которой происходит поиск
    Returns:
        True/False в зависимости от корректности/некорректности расстановки строк
    """

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