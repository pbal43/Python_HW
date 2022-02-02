# HW по Python CRUD
#
# Доделать то, что начали на занятии по CRUD
# На занятии мы сделали Create, Read
# Теперь надо доделать Update, Delete.
#
#  1. Сделать функционал для проверки уникальности Email (существует ли такой пользователь) перед добавлением нового пользователя.
#  2. Добавить возможность обновления информации о существующем пользователе.
#  3. Добавить возможность удалить существующего пользователя
#  4. Сделать -- Help для просмотра списка возможных команд с комментариями к ним

from create import create_user
from read import user_info, all_users_info
from update import update_func
from delete import del_func
from help import help_func
import re
user_emails=[]
users_storage = {}

while True:
    action = str.lower(str.strip(input('enter action (create, read_all, read_user, update, delete), --help для помощи  ')))
    if action == 'create':
        print('action = ', action)
        email = str.lower(str.strip(input('Email: ')))
        if email not in user_emails and email != "":
            name = input('Name: ')
            if name == "":
                print('Пустое поле, введите имя')
                continue
            password = input('Введите Password (более 4 символов, обязательны цифры и латинница верхним регистром): ')
            if password == "":
                print('Пустое поле, введите password')
                continue
            if len(password) <= 4 or  (re.search('[0-9]',password) is None) or (re.search('[A-Z]',password) is None):
                print('Password не соответствует требованиям')
                continue
            phone = input('Phone: ')
            if phone == "":
                print('Пустое поле, введите phone')
                continue
            create_user(email,
                        name,
                        password,
                        phone,
                        user_emails,
                        users_storage)
            print('user_emails', user_emails)
            print('users_storage', users_storage)
        else:
            print('this user already exist or empty input')
    elif action == 'read_all':
        print('action = ', action)
        all_users_info(users_storage)
    elif action == 'read_user':
        user_e = str.lower(str.strip(input('Enter user email  ')))
        print('action = ', action)
        user_info(user_e, user_emails, users_storage)
    elif action == 'update':
        print('action = ', action)
        user_em = str.lower(str.strip(input('Enter user email  ')))
        update_func(user_em, user_emails, users_storage)
    elif action == 'delete':
        print('action = ', action)
        del_mail = str.lower(str.strip(input('Выберете аккаунт для удаления (введите email)')))
        del_func(del_mail, user_emails, users_storage)
    elif action == '--help':
        help_func()
    else:
        print('Please enter valid command')

