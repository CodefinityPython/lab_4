# Декоратор для перевірки, чи користувач зареєстрований

def user_registered(func):
    def wrapper(username, data):
       if username in registered_users:
           return func(username, data)
       else:
           return f"Access denied, {username} is not registered"
    return wrapper   


# Приклад використання декоратора
