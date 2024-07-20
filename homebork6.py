#2. Работа со словарями:
my_dict = {'Nikita': 1987, 'Oleg': 2001, 'Sergey': 1964}

print(my_dict)

my_dict.get('Nikita', 'Kristina')
my_dict.get('Kristina')
my_dict.update({'Artem': 1957,
                'Fedor': 1990})
print(my_dict)

del my_dict['Sergey']

print(my_dict)

#3. Работа с множествами:

my_set = {1,1,'Karina','Karina',4.1,4.1,}

print(my_set)

my_set.add(5)

my_set.add(6)

print(my_set)

my_set.discard(1)

print(my_set)