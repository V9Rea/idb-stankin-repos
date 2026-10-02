import re

pattern_order = r'(?:заказ|order|номер[\s_]+заказа)(?:[\s_]*[№No]+)?[:\s]*([А-Яа-яA-Za-z0-9-]+)'
pattern_sku = r'(?:sku|артикул)[:\s]*([А-Яа-яA-Za-z0-9-]+)'
def read(file_path: str) -> list[str]:
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            lines.append(line.strip())

    return lines

def search_article(lines: list[str]):
    for index, line in enumerate(lines):
        order = re.search(pattern_order,line, re.IGNORECASE).group(1)
        sku = re.search(pattern_sku, line, re.IGNORECASE).group(1)
        print(f'line {index}: заказ - {order:<10}, артикул - {sku}')

def main():
    path = "source.txt"
    lines = read(path)
    search_article(lines)

if __name__ == '__main__':
    main()