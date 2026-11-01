import random
import csv


#Проверка авторов
with open('books.csv', encoding = 'cp1251') as f:
    reader = csv.DictReader(f, delimiter=';')
    authors = set()
    for line in reader:
        authors.add(line['Автор'].strip())

for author in sorted(authors):
    print(author)


#№1
def count_titles(csv_file, needed_len = 30):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter = ';')
    counter = 0
    for line in reader:
        title = line['Название'].strip()
        if len(title) > needed_len:
            counter += 1
    return counter


#№2
def find_by_author(csv_file, author_name, min_price = 200.0):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter = ';')
    results = []
    for line in reader:
        authors = line['Автор'].strip()
        price = float(line['Цена поступления'])
        if author_name in authors and price >= min_price:
            year = line['Дата поступления'].split('.')[-1].split()[0]
            results.append({
                'Автор': authors,
                'Название': line['Название'].strip(),
                'Год': year,
                'Цена': price,
            })
    return results



#№3
def generate_references(csv_file, output_file = 'references.txt', counter = 20):
    csv_file.seek(0)
    reader = csv.DictReader(csv_file, delimiter = ';')
    lines = list(reader)
    sample = random.sample(lines, min(counter, len(lines)))
    with open(output_file, 'w', encoding = 'utf-8') as f:
        for number, line in enumerate(sample, start = 1):
            author = line["Автор"].strip()
            title = line["Название"].strip()
            year = line["Дата поступления"].split('.')[-1].split()[0]
            line = f'{number}. {author}. {title} - {year}\n'
            f.write(line)
    return output_file


if __name__ == '__main__':
    with open('books.csv', encoding = 'cp1251') as f:
        counter = count_titles(f, needed_len = 30)
        print('№1: Книг с названием, длина которого больше 30 символов:', counter)


        author = input('Автор для поиска:').strip()
        books = find_by_author(f, author, min_price = 200.0)
        if books:
            for i in books:
                print(f"№2: {i['Автор']} - {i['Название']} ({i['Год']}) - {i['Цена']} руб.")
        else:
            print('№2: Книг по такому автору нет')


        file = generate_references(f, output_file = 'references.txt', counter = 20)
        print(f'№3: Библиографические ссылки сохранены в файл {file}')


    with open('references.txt', encoding = 'utf-8') as ref_file:
        print(ref_file.read())