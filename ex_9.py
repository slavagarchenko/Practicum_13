def convert_date_time(date_time_str):
    """
    Convert date and time string from "MM/DD/YYYY HR:MIN:SEC" format to "DD.MM.YY HR:MIN:SEC"
    
    Args:
        date_time_str (str): Date and time string in "MM/DD/YYYY HR:MIN:SEC" format
    Returns:
        None
    """
    try:
        if len(date_time_str.split()) != 2:
            print("Неверно введен формат даты-времени")
            return
        
        date_part, time_part = date_time_str.split()
        
        date_components = date_part.split('/')
        if len(date_components) != 3:
            print("Неверный формат даты")
            return
        
        month, day, year = date_components
        
        if not (month.isdigit() and day.isdigit() and year.isdigit()):
            print("Месяц, день и год должны быть числами")
            return
        
        month = int(month)
        day = int(day)
        year = int(year)
        
        if month < 1 or month > 12:
            print("Месяц должен быть от 1 до 12")
            return
        
        days_in_month = {
            1: 31, 
            2: 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28,
            3: 31, 
            4: 30, 
            5: 31, 
            6: 30, 
            7: 31, 
            8: 31, 
            9: 30, 
            10: 31, 
            11: 30, 
            12: 31
        }
        
        if day < 1 or day > days_in_month[month]:
            print(f"В месяце {month} не может быть {day} дней")
            return
        
        if year < 1000 or year > 9999:
            print("Год должен быть четырехзначным числом")
            return
        
        time_components = time_part.split(':')
        if len(time_components) != 3:
            print("Неверный формат времени")
            return
        
        hour, minute, second = time_components
        
        if not (hour.isdigit() and minute.isdigit() and second.isdigit()):
            print("Часы, минуты и секунды должны быть числами")
            return
        
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        
        if hour < 0 or hour > 23:
            print("Часы должны быть от 0 до 23")
            return
        
        if minute < 0 or minute > 59:
            print("Минуты должны быть от 0 до 59")
            return
        
        if second < 0 or second > 59:
            print("Секунды должны быть от 0 до 59")
            return

        total_seconds = 0

        for i in range(1, month):
            total_seconds += days_in_month[i] * 24 * 3600

        total_seconds +=(day-1) * 24 * 3600

        total_seconds += hour * 3600 + minute *60 + second

        return total_seconds
    
    except Exception as e:
        print(f"Ошибка обработки: {e}")
        return None


data = input("Введите дату и время (MM/DD/YYYY HR:MIN:SEC): ")
seconds = seconds_in_year(data)

