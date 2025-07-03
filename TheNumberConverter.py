from datetime import datetime

class Task1:
    def __init__(self):
        self.data = []
    
    def get_valid_input(self, prompt, error_message):
        while True:
            value = input(prompt)
            if value.isdigit():
                return value
            print(error_message)
    
    def collect_data(self):
        day = self.get_valid_input('Привет, введите день своего рождения: ', 'Пожалуйста введите значение цифрами')
        month = self.get_valid_input('А теперь введи месяц своего рождения: ', 'Пожалуйста введите значение цифрами')
        year = self.get_valid_input('И последнее. Введи год своего рождения: ', 'Пожалуйста введите значение цифрами')
        self.data = [day, month, year]
    
    def analyze(self):
        if not self.data:
            print("Данные не введены!")
            return
        
        self.day_of_week()
        self.check_year()
        self.age_of_user()
        self.table_check()
    
    def day_of_week(self):
        try:
            day_int = int(self.data[0])
            month_int = int(self.data[1])
            year_int = int(self.data[2])
            birth_date = datetime(year_int, month_int, day_int)
            
            weekdays = [
                "Понедельник", "Вторник", "Среда", 
                "Четверг", "Пятница", "Суббота", "Воскресенье"
            ]
            
            weekday_name = weekdays[birth_date.weekday()]
            print(f"День недели когда вы появились на свет, был: {weekday_name}")

        except ValueError:
            print("Ошибка: Введена некорректная дата!")
    
    def check_year(self):
        year = int(self.data[2])
        is_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        print('Год был високосный' if is_year else 'Год был не високосный')
    
    def age_of_user(self):
        try:
            today = datetime.now()
            birth_day = int(self.data[0])
            birth_month = int(self.data[1])
            birth_year = int(self.data[2])
            birth_date = datetime(birth_year, birth_month, birth_day)
            
            age = today.year - birth_date.year
            if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
            
            print(f"Сейчас вам {age} полных лет")
        
        except ValueError as e:
            print(f"Ошибка вычисления возраста: {e}")
    
    def table_check(self):
        day_str = self.data[0].zfill(2)
        month_str = self.data[1].zfill(2)
        year_str = self.data[2].zfill(4)
        full_date = day_str + month_str + year_str

        digit_patterns = {
            '0': ["***", "* *", "* *", "* *", "***"],
            '1': [" * ", "** ", " * ", " * ", "***"],
            '2': ["***", "  *", "***", "*  ", "***"],
            '3': ["***", "  *", "***", "  *", "***"],
            '4': ["* *", "* *", "***", "  *", "  *"],
            '5': ["***", "*  ", "***", "  *", "***"],
            '6': ["***", "*  ", "***", "* *", "***"],
            '7': ["***", "  *", " * ", " * ", " * "],
            '8': ["***", "* *", "***", "* *", "***"],
            '9': ["***", "* *", "***", "  *", "***"]
        }

        print('\nДата вашего рождения в виде электронного табло')
        for row in range(5):
            line_parts = []
            for i, char in enumerate(full_date):
                if i == 2 or i == 4:
                    line_parts.append("  ")
                line_parts.append(digit_patterns[char][row] + "  ")
            print(''.join(line_parts))

def main():
    analyzer = Task1()
    analyzer.collect_data()
    analyzer.analyze()

if __name__ == "__main__":
    main()