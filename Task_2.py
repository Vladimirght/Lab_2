import xml.etree.ElementTree as ET


def parse_currency(xml_file):
    tree = ET.parse(xml_file) #дерево - функция сама может работать с файлом, можно указать в скобочках относительный путь и не открывать вручную
    print(tree)
    root = tree.getroot() #корневой элемент
    print(root)
    num_codes = []
    char_codes = []
    for valute in root.findall('Valute'):
        num_code = valute.find('NumCode').text.strip() #находит единствнный дочерний элемент NumCode из Valute и берет из него только текст, удаляя пробелы или переносы
        char_code = valute.find('CharCode').text.strip()
        num_codes.append(num_code)
        char_codes.append(char_code)
    return num_codes, char_codes


if __name__ == '__main__':
    with open('currency.xml', 'rb') as f: #бинарный режим открытия, чтобы не было проблем с кодировками
        num_codes, char_codes = parse_currency(f)

    print('NumCode:', num_codes)
    print('CharCode:', char_codes)
    print('Всего:', len(num_codes))


#Приедение не нужно, оба списка хранят строки, т.к. '036' станет 36. Если бы это было нужно,
#то надо было бы обратить int/float и заменить запятые на точки