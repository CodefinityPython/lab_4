# Список імен зареєстрованих користувачів
registered_users = ["User1", "User2", "User3"]


# Декоратор для перевірки, чи користувач зареєстрований

def user_registered(func):
    def wrapper(username, data):
        if username in registered_users:
            return func(username, data)
        else:
            return f"Access is denied, {username} isn`t registered"
    return wrapper
#



# Приклад використання декоратора
@user_registered
def access_sensitive_data(username, data):
    return f"Accessing sensitive data for {username}: {data}"


# Приклади викликів функції з різними користувачами
current_user = "User1"
data_to_access = "Some sensitive information"

# Доступ має бути наданий
print(access_sensitive_data(current_user, data_to_access))


current_user = "User4"
data_to_access = "Confidential data"

# Доступ має бути відмовлено, оскільки користувач не зареєстрований
print(access_sensitive_data(current_user,data_to_access))