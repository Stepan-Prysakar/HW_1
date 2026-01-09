import re

def normalize_phone(phone_number):

    # Видаляємо зайвий синтаксис:
    patern_dell_symbols = r"[\[\];,\-:!\.tnrfn\\=\s()]" # як додати в шаблон видалення всіх букв? (a-zA-Z - тільки латинські)?
    repl_dell_symbols = ''
    number = re.sub(patern_dell_symbols, repl_dell_symbols, phone_number)
    if number.startswith('+380'):
        return number
    else:
        number = number.removeprefix('8')
        number = number.removeprefix('38')
        number = number.removeprefix('+38')
        number = '+38' + number
        return number

raw_numbers = "38050 111 22 11  "
print(normalize_phone(raw_numbers))