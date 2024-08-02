def print_params(a=1, b='string', c=True):
    print(a, b, c)


# Создайте список values_list с тремя элементами разных типов.
values_list = [100, 'Mom', False]
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
values_dict = {'a': 3, 'b': 'int', 'c': False}
# Создайте список values_list_2 с двумя элементами разных типов
values_list_2 = [32, 'Dad']
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
print_params(12, 'number')
print_params(12)
print_params()
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
print_params(b=25)
print_params(c=[1, 2, 3])
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
print_params(*values_list)
print_params(**values_dict)
# Проверьте, работает ли print_params(*values_list_2, 42)
print_params(*values_list_2, 42)