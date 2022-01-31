def update_func(user_em, user_emails, users_storage):
    if user_em in user_emails:
        while True:
            new_data = input('Что вы желаете заменить? (Введите: "email", "name", "password", "phone")\nДля выхода введите "S"')
            if new_data == 'email':
                user_em_new = input('Введите новое значение Email (для сохранения старого - введите старое)\nпосле смены email для изменения других данных необходимо вызвать функцию заново')
                a = user_emails.index(user_em)
                user_emails[a] = user_em_new
                users_storage[user_em_new] =  users_storage.pop(user_em)
                print('Новый email =', user_em_new)
                break
            if new_data == 'name':
                user_name_new = input('Введите новое значение name (для сохранения старого - введите старое)')
                users_storage[user_em]['name'] = user_name_new
                print('Новое name =', user_name_new)
            if new_data == 'password':
                user_pass_auth = input('введите старый пароль')
                if user_pass_auth == users_storage[user_em]['password']:
                    new_pass = input('Введите новый пароль (для сохранения старого - введите старый)')
                    users_storage[user_em]['password'] = new_pass
                    print('Новый password =', new_pass)
                else:
                    print('wrong pass')
            if new_data == 'phone':
                user_phone_new = input('Введите новое значение phone (для сохранения старого - введите старый)')
                users_storage[user_em]['phone'] = user_phone_new
                print('Новый phone=', user_phone_new)
            elif new_data == 'S':
                print('операция отменена')
                break
    else:
        print('unknown email')