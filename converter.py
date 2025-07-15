import datetime

def get_day_of_week(day, month, year):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[datetime.date(year, month, day).weekday()]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birth_day, birth_month, birth_year):
    today = datetime.date.today()
    age = today.year - birth_year
    if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
        age -= 1
    return age

def print_digital_style(date_str):
    digit_patterns = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': ['  *', '  *', '  *', '  *', '  *'],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', '***', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['***', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '***'],
        ' ': ['   ', '   ', '   ', '   ', '   ']
    }
    
    for line in range(5):
        for char in date_str:
            print(digit_patterns.get(char, digit_patterns[' '])[line], end=' ')
        print()

def main():
    print("Введите дату вашего рождения")
    day = int(input("День: "))
    month = int(input("Месяц: "))
    year = int(input("Год: "))
    
    print("\nРезультаты:")
    print(f"День недели: {get_day_of_week(day, month, year)}")
    print(f"Год {'високосный' if is_leap_year(year) else 'не високосный'}")
    print(f"Вам {calculate_age(day, month, year)} лет")
    
    date_str = f"{day:02d} {month:02d} {year}"
    print("\nДата рождения в цифровом стиле:")
    print_digital_style(date_str)

if __name__ == "__main__":
    main()