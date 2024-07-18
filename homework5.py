immutable_var = 1,2,3,4,True,'string'
print(immutable_var)
#immutable_var [0] = 1 # Выводит ошибку из за того что не может менять элементы кортежа
mutable_list = ['город','улица','район','микро-район']
mutable_list[0] = 'мегаполис'
print(mutable_list)
