def number(num):
    password = []
    for i in range(1, num + 1):
        for j in range(i + 1, num + 1):
            sum = i + j
            if num % sum == 0:
                password.append(i)
                password.append(j)
    return password


num = int(input('Введите то число что на камне: '))
password = number(num)
print('Пароль: ', *password, sep='')
