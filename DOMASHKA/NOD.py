def nod(a, b):
    if a <= 0 or b <= 0:
        return 0  

    while b:
        a, b = b, a % b

    return a  

try:
    a = int(input("Введите первое натуральное число: "))
    b = int(input("Введите второе натуральное число: "))
    
    result = nod(a, b)
    if result == 0:
        print("Невалидный ввод. Пожалуйста, введите натуральные числа.")
    else:
        print(f"Наибольший общий делитель: {result}")
except ValueError:
    print("Невалидный ввод. Пожалуйста, введите натуральные числа.")
