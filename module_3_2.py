def send_email(a, b, c='university.help@gmail.com'):
    correct_domen = ('.com', '.ru', '.net')
    valid = b.endswith(correct_domen) == c.endswith(correct_domen)
    if b.count('@') and c.count('@'):
        if valid is not True:
            print(f'Невозможно отправить письмо с адреса {c} на адрес {b}')
        elif b == c:
            print("Нельзя отправить письмо самому себе!")
        elif c == 'university.help@gmail.com':
            print(f"Письмо успешно отправлено с адреса {c} на адрес {b}.")
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {c} на адрес {b}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', c='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', c='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', c='urban.teacher@mail.ru')

