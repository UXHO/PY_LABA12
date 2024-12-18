def sort_by_key(item):
    return item[0]


def sort_by_value(item):
    return item[1]


file = open("surname_year_input.txt", "r", encoding='utf-8')
lines = [line.strip().split(" ") for line in file]
file.close()


dct = {lines[i][0]: lines[i][1] for i in range(len(lines))}
print("Словарь: ", dct)


dct1 = dict(sorted(dct.items(), key=sort_by_key))
print("Первая сортировка: ", dct1)


dct2 = dict(sorted(dct1.items(), key=sort_by_value, reverse=True))
print("Вторая сортировка: ", dct2)
