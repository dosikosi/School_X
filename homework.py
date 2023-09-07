def find_square_root(num):
    if num <= 1:
        return num
    x = 2
    y = num // 2
    while x <= y:
        mid = (x + y) // 2
        square = mid * mid
        if square == num:
            return mid
        elif square < num:
            x = mid + 1
        else:
            y = mid - 1
    print("Слишком сложно, не могу")
    return None
try:
    num = int(input("Введите натуральное число: "))
    result = find_square_root(num)
    if result is not None:
        print(f"Корень числа {num} равен {result}")
except ValueError:
    print("Ошибка: Введите натуральное число.")
