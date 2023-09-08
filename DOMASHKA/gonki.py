from typing import Dict, Any

from import_this import RACE_DATA

def format_time(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def print_winner_and_top_three(data: Dict[str, Dict[str, Any]]) -> None:
    SORTED_RESULTS = sorted(data.items(), key=lambda x: x[1]['FinishedPlace'])

    WINNER_NAME = SORTED_RESULTS[0][1]['RacerName'].upper()
    WINNER_MESSAGE = f"Выиграл - {WINNER_NAME}!!! Поздравляем!!"
    print(WINNER_MESSAGE)
    print("_" * len(WINNER_MESSAGE))

    print("\nПервые три места:\n")
    for i in range(3):
        RACER_DATA = SORTED_RESULTS[i][1]
        PLACE = RACER_DATA['FinishedPlace']
        NAME = RACER_DATA['RacerName']
        TEAM = RACER_DATA['RacerTeam']
        TIME = RACER_DATA['FinishedTimeSeconds']

        FORMATTED_TIME = format_time(TIME)

        print(f"Гонщик на {PLACE} месте:")
        print(f"    Имя: {NAME}")
        print(f"    Команда: {TEAM}")
        print(f"    Время: {FORMATTED_TIME} \n")

if __name__ == "__main__":
    print_winner_and_top_three(RACE_DATA)
