def sort_by_key(item):
    return item[0]


def sort_by_value(item):
    return item[1]


# Open the file manually
file = open("surname_year_input.txt", "r", encoding='utf-8')
lines = [line.strip().split(" ") for line in file]
file.close()  # Close the file after reading

# Create a dictionary from the lines
dct = {lines[i][0]: lines[i][1] for i in range(len(lines))}
print("Словарь: ", dct)

# Sort the dictionary by key
dct1 = dict(sorted(dct.items(), key=sort_by_key))
print("Первая сортировка: ", dct1)

# Sort the dictionary by value in descending order
dct2 = dict(sorted(dct1.items(), key=sort_by_value, reverse=True))
print("Вторая сортировка: ", dct2)
