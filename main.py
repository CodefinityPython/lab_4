# Список імен зареєстрованих користувачів
registered_users = ["user1", "user2", "user3"]

# створюю декоратор для перевірки
def user_registered(func): 
    def inner(user, data):
        if registered_users.__contains__(user):
            return func(user, data)
        else:
            return 'You have entered incorrct information!'
    return inner

# Приклад використання декоратора

@user_registered
def access_sensitive_data(username, data):
    return f"Accessing sensitive data for {username}: {data}"

# Доступ має бути наданий

current_user = "user1"
data_to_access = "Special information"
print(access_sensitive_data(current_user, data_to_access))

# Доступ має бути відмовлено, оскільки користувач не зареєстрований
current_user = "user4"
data_to_access = "Confidential data"

print(access_sensitive_data(current_user,data_to_access))



            