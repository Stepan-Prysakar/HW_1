import random

def get_numbers_ticket(min, max, quantity):

    if min>=1 and max<=1000 and (max-min) >= quantity: # перевірка коректності вхідних даних та забезпечення умови унікальності для random.sample
        lottery_numbers = sorted(random.sample(range(min, max), quantity)) # відсортований список випадкових чисел
        return lottery_numbers
    else:
        return [] # вивід при невідповідності вхідних параметрів

print("Ваші лотерейні числа:", get_numbers_ticket(1, 60, 5))
