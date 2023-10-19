# Список імен зареєстрованих користувачів
registered_users = ["user1", "user2", "user3"]


# Декоратор для перевірки, чи користувач зареєстрований
def user_registered(func):
    def wrapper(usersname, data):
        is_registered = True
        if is_registered:
            return func(usersname, data)
        else:
            return "User is not registered."
    return wrapper

# Example usage of the decorator:
@user_registered
def some_protected_function():
    return "This is a protected function."

# Test cases
registered_user = some_protected_function()
unregistered_user = some_protected_function()

print(registered_user)
print(unregistered_user)

# Приклад використання декоратора
@user_registered
def access_sensitive_data(username, data):
    return f"Accessing sensitive data for {username}: {data}"


# Приклади викликів функції з різними користувачами
current_user = "user1"
data_to_access = "Some sensitive information"

# Доступ має бути наданий
print(access_sensitive_data(current_user, data_to_access))


current_user = "user4"
data_to_access = "Confidential data"

# Доступ має бути відмовлено, оскільки користувач не зареєстрований
print(access_sensitive_data(current_user,data_to_access))