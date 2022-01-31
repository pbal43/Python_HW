def del_func(del_mail, user_emails, users_storage):
    if del_mail in user_emails:
        while True:
            auth = input('Для удаления аккаунта - введите пароль, для отмены - введите "S"')
            if auth == users_storage[del_mail]['password']:
                user_emails.remove(del_mail)
                users_storage.pop(del_mail)
                print('Аккаунт', del_mail, 'успешно удален')
                break
            if auth == 'S':
                print('Операция отменена')
                break
            else:
             print('wrong password')
    else:
        print('unknown email')
