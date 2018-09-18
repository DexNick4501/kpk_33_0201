from pizza import Pizza, Snacks, Drinks

print('*' *25)
pizza = Pizza.import_from_file('pizzas.src')
[print(el) for el in pizza]

print('*' *25)
snacks = Snacks.import_from_file('snackses.src')
[print(el) for el in snacks]

print('*' *25)
drinks = Drinks.import_from_file('drinkses.src')
[print(el) for el in drinks]