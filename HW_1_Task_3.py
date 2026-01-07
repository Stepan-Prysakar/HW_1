import re

def normalize_phone(phone_number):

    # Видаляємо зайвий синтаксис:
    patern_dell_symbols = r"[\[\];,\-:!\.tnrfn\\=\s()]" # як додати в шаблон видалення всіх букв? (a-zA-Z - тільки латинські)?
    repl_dell_symbols = ''
    phone_number_dell_symbols = re.sub(patern_dell_symbols, repl_dell_symbols, str(phone_number))
  
    # Перетворюємо рядок phone_number_dell_symbols на список рядкових об'єктів, по яких буде проходити цикл for для подальшого форматування:
    patern_list = r'[\']+'
    phone_number_list = re.split(patern_list, phone_number_dell_symbols)[1:-1] # [1:-1] - ігноруємо елементи ('') на початку та вкінці
   
    # Ініціалізуємо список та наповнюємо його відформатованими номерами:
    list_numbers = []
    for num in phone_number_list:
        num = num.removeprefix('8') # видаляємо можливі варіанти запису коду країни, приводячи всі номери до одного формату
        num = num.removeprefix('38')
        num = num.removeprefix('+38')
        num = '+38' + num # додаємо однаковий формат запису коду країни для всіх номерів
        list_numbers+=[num]
    return list_numbers


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
print(normalize_phone(raw_numbers))