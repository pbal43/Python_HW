from create import create_user
from read import user_info, all_users_info
from update import update_func
from delete import del_func
from help import help_func
user_emails=[]
users_storage = {}



while True:
    action = input('enter action (create, read_all, read_user, update, delete), --help для помощи  ')
    if action == 'create':
        print('action = ', action)
        email = input('Email: ')
        if email not in user_emails:
            name = input('Name: ')
            password = input('Password: ')
            phone = input('Phone: ')
            create_user(email,
                        name,
                        password,
                        phone,
                        user_emails,
                        users_storage)
            print('user_emails', user_emails)
            print('users_storage', users_storage)
        else:
            print('this user already exist')
    elif action == 'read_all':
        print('action = ', action)
        all_users_info(users_storage)
    elif action == 'read_user':
        user_e = input('Enter user email  ')
        print('action = ', action)
        message = user_info(user_e, user_emails, users_storage)
        print('User:', message)
    elif action == 'update':
        print('action = ', action)
        user_em = input('Enter user email  ')
        update_func(user_em, user_emails, users_storage)
    elif action == 'delete':
        print('action = ', action)
        del_mail = input('Выберете аккаунт для удаления (введите email)')
        del_func(del_mail, user_emails, users_storage)
    elif action == '--help':
        help_func()
    else:
        print('Please enter valid command')

