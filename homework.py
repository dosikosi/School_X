def find_integer_square_root(num):
    if num <= 1:
        return num
    low = 2
    high = num // 2
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square == num:
            return mid
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1
    print("Слишком сложно, не могу")
    return None
try:
    num = int(input("Введите натуральное число: "))
    result = find_integer_square_root(num)
    if result is not None:
        print(f"Корень числа {num} равен {result}")
except ValueError:
    print("Ошибка: Введите натуральное число.")
