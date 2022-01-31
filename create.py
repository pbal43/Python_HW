def create_user(email, name, password, phone, user_emails, users_storage):
    user_emails.append(email)
    users_storage[email] = {'name': name,
                            'password': password,
                            'phone': phone}
    return None