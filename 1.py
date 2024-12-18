import random
import time

# Генерация массива из 1000 случайных чисел от 1 до 10000
random_array = [random.randint(1, 10000) for _ in range(1000)]


# Функция пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Копируем массив для каждого теста
random_array_copy = random_array.copy()

# Измерение времени пузырьковой сортировки
start_time = time.time()
bubble_sorted_array = bubble_sort(random_array_copy)
bubble_sort_time = time.time() - start_time

# Измерение времени стандартной сортировки
start_time = time.time()
sorted_array = sorted(random_array)
sorted_sort_time = time.time() - start_time

print(f"Время работы пузырьковой сортировки: {bubble_sort_time:.6f} секунд")
print(f"Время работы стандартной сортировки: {sorted_sort_time:.6f} секунд")
