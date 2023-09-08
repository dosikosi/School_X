from import_this import RACE_DATA

sorted_results = sorted(RACE_DATA.items(), key=lambda x: x[1]['FinishedPlace'])

print("Выиграл -", sorted_results[0][1]['RacerName'].upper() + "!!! Поздравляем!!")
print("_______________________________")
print("\nПервые три места:\n")

for i in range(3):
    place = sorted_results[i][1]['FinishedPlace']
    name = sorted_results[i][1]['RacerName']
    team = sorted_results[i][1]['RacerTeam']
    time = sorted_results[i][1]['FinishedTimeSeconds']

    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

    print(f"Гонщик на {place} месте:")
    print(f"    Имя: {name}")
    print(f"    Команда: {team}")
    print(f"    Время: {formatted_time} \n")
