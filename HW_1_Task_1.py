from datetime import datetime

def get_days_from_today(date):

    try: # Обробляємо винятки за допомогою конструкції try-except
        date_date_object = datetime.strptime(date, '%Y-%m-%d').date() # перетворюємо вхідний рядок в об'єкт datetime 
        today = datetime.today().date() 
        diff_days = (today - date_date_object).days # обчислюємо різницю в днях
        return diff_days
    
    except ValueError:
        return 'Enter the date in the "YYYY-MM-DD"-format please.' # вивід при некоректному форматі вхідних даних

date = '2020-10-09'
print(get_days_from_today(date))