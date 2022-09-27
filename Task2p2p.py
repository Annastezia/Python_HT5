from random import randint

def print_name(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def player(name, n, counter, candies):
    print(f"Ходил {name}, он взял {n}, теперь у него {counter}. Осталось на столе {candies} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")

candies = int(input("Введите количество конфет на столе: "))
queue = randint(0,2)
if queue:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while candies > 28:
    if queue:
        n = print_name(player1)
        counter1 += n
        candies -= n
        queue = False
        player(player1, n, counter1, candies)
    else:
        k = print_name(player2)
        counter2 += n
        candies -= n
        queue = True
        player(player2, n, counter2, candies)

if queue:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")