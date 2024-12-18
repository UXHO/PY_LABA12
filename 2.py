# Функция для подсчета количества вхождений буквы "а"
def count_letter_a(linee):
    return linee.count('а')


try:
    file = open('input.txt', 'r', encoding='utf-8')
except FileNotFoundError:
    print("Ошибка: файл не найден.")
    exit()
else:
    lines = file.readlines()
    file.close()
    print("Текст успешно прочитан из файла.")


# Сортировка строк по количеству вхождений буквы "а"
sorted_lines = sorted(lines, key=count_letter_a, reverse=True)


file = open('output.txt', 'w', encoding='utf-8')
file.writelines(sorted_lines)
file.close()

for line in sorted_lines:
    print(line.strip())
