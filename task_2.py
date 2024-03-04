def binary_search_with_upper_bound(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = arr[-1]  # Початкове значення - максимальний елемент масиву

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return iterations, upper_bound


if __name__ == "__main__":
    # Тестування функції
    arr = [1.1, 1.3, 2.5, 3.8, 4.6, 5.9]
    print(
        binary_search_with_upper_bound(arr, 15.1)
    )  # Виведе: (кількість ітерацій, верхню межу)
    print(
        binary_search_with_upper_bound(arr, 4)
    )  # Виведе: (кількість ітерацій, верхню межу)
    print(
        binary_search_with_upper_bound(arr, 6.0)
    )  # Виведе: (кількість ітерацій, максимальний елемент)
