def user_info(email, user_emails, users_storage):
    if email in user_emails:
        message = 'user_email =', email, 'user_info:', users_storage[email]
    else:
        message = 'no user with email:', email
    print('User info:', message)

def all_users_info(users_storage):
    for k, v in users_storage.items():
        user_email = 'User email: ' + k
        user_info_1 = 'User info: ', v
        print(user_email, user_info_1)

