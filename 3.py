# Чтение данных из файла
try:
    file = open('surname_year_input.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Ошибка: файл не найден.")
    exit()
else:
    lines = file.readlines()
    file.close()
    print("Текст успешно прочитан из файла.")

# Сохранение данных в список словарей
data = []
for line in lines:
    surname, year_of_birth = line.strip().split()
    data.append({'Фамилия': surname, 'Год рождения': int(year_of_birth)})


# Сортировка данных
def sort_key(item):
    return item['Фамилия'], item['Год рождения']


sorted_spisok = sorted(data, key=sort_key)

for f_y in sorted_spisok:
    print(f_y)
