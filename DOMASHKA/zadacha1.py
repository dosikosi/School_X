first_igrok = input('Игрок 1: ')
second_igrok = input('Игрок 2: ')

valid_choices = {'камень', 'ножницы', 'бумага'}

if first_igrok not in valid_choices or second_igrok not in valid_choices:
    print('Пожалуйста, введите только слова "камень", "ножницы" или "бумага".')
else:
    if first_igrok == second_igrok:
        print('Ничья')
    elif (
        (first_igrok == 'камень' and second_igrok == 'ножницы') or
        (first_igrok == 'ножницы' and second_igrok == 'бумага') or
        (first_igrok == 'бумага' and second_igrok == 'камень') 
    ):
        print('Игрок 1 выиграл')
    else:
        print('Игрок 2 выиграл')
