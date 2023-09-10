def convert_seconds_to_hours_and_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours} час(а/ов) и {minutes} минут(а/ы)"

seconds = int(input("Введите количество секунд: "))

result = convert_seconds_to_hours_and_minutes(seconds)
print(result)
