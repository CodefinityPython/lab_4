# Функція для перевірки, чи користувач зареєстрований
def is_user_registered(username):
    # Перевірка, чи користувач зареєстрований (ваша реалізація)
    # Повертає True, якщо користувач зареєстрований, і False в іншому випадку
    registered_users = ["user1", "user2", "user3"]  # Приклад зареєстрованих користувачів
    return username in registered_users

# Декоратор "user_registered"
def user_registered(view_func):
    def wrapper(username, *args, **kwargs):
        if is_user_registered(username):
            # Якщо користувач зареєстрований, викликаємо функцію view_func
            return view_func(username, *args, **kwargs)
        else:
            return "Доступ заборонений. Користувач не зареєстрований."

    return wrapper

# Приклад використання декоратора "user_registered"
@user_registered
def my_protected_page(username):
    return f"Ласкаво просимо, {username}! Ця сторінка доступна тільки зареєстрованим користувачам."

# Виклик сторінки (захищена сторінка)
username = "user1"  # Зареєстрований користувач
result = my_protected_page(username)
print(result)

# Виклик сторінки (користувач не зареєстрований)
username = "guest"  # Незареєстрований користувач
result = my_protected_page(username)
print(result)
