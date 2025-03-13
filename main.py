def merge_sort(arr):
    """
    Функция для сортировки массива с использованием сортировки слиянием.
    """
    # Базовый случай: если массив содержит 1 элемент или пуст, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Рекурсивно разделяем массив на две половины
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Сливаем две отсортированные половины
    return merge(left_half, right_half)

def merge(left, right):
    """
    Функция для слияния двух отсортированных массивов в один отсортированный массив.
    """
    sorted_array = []
    i = j = 0

    # Слияние элементов из left и right в sorted_array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из left (если они есть)
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # Добавляем оставшиеся элементы из right (если они есть)
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

arr = [38, 27, 43, 3, 9, 82, 10]
print("Исходный массив:", arr)

sorted_arr = merge_sort(arr)
print("Отсортированный массив:", sorted_arr)


# 1. Логарифмическая сложность
# Алгоритм:
# Предполагаем, что массив отсортирован.
# Находим средний элемент массива.
# Если средний элемент равен искомому, возвращаем его индекс.
# Если средний элемент больше искомого, повторяем поиск в левой половине массива.
# Если средний элемент меньше искомого, повторяем поиск в правой половине массива.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Элемент найден
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return -1  # Элемент не найден

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
print(binary_search(arr, target))  # 3 (индекс элемента 7)