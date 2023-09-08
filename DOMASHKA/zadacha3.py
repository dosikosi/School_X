input_str = input('Введите массив чисел через пробел: ')
input_list = input_str.split()
numbers = [int(x) for x in input_list]

index = []

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1] + 1:
        index.append(i)

if not index:
    print("Не найдено")
elif len(index) == 1:
    print(index[0])
else:
    print(index)
