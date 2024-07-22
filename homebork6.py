#2. Работа со словарями:
my_dict = {'Nikita': 1987, 'Oleg': 2001, 'Sergey': 1964}

print('Dict',my_dict)

print(('Existing value:'),my_dict.get('Nikita'))

print(('Not existing value:'), my_dict.get('Kristina'))

my_dict.update({'Artem': 1957,
                'Fedor': 1990})

print(('Deleted value:'),my_dict.pop('Sergey'))


print(('Modified dictionary:'),my_dict)


#3. Работа с множествами:

my_set = {1,1,'Karina','Karina',4.1,4.1,}

my_set.add(5)

my_set.add(6)

print(('Modified set:'),my_set)

my_set.discard(1)

print(('Set:'), my_set)
