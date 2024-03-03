def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0

    while low <= high:
        i += 1

        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return i, arr[mid]

    # якщо елемент не знайдений
    return -1


arr = [2.3, 3, 3.3, 4, 10.2, 40]
x = 3.3
result = binary_search(arr, x)
if result != -1:
    print(f"{result}")
else:
    print("Element is not present in array")
