import random

# randomowa liczba od zakresu z zakresu [0, 1)
random_number = random.random()
print(random_number)

# randomowa liczba całkowita z zakresu [X, Y)
random_integer = random.randint(1, 10)
print(random_integer)

# randomowa liczba zmiennoprzecinkowa z zakresu [X, Y)
random_float = random.uniform(1.5, 5.5)
print(random_float)

# randomowa liczba całkowita z zakresu [X, Y) ale z krokiem danym
random_number = random.randrange(0, 20, 2)
print(random_number)

# randomowa liczba z listy
choices = [1, 2, 3, 4, 5]
random_choice = random.choice(choices)
print(random_choice)

# K randomowych liczb z danego zbioru liczb
random_sample = random.sample([1, 2, 3, 4, 5], 3)
print(random_sample)

