# Список імен зареєстрованих користувачів
registered_users = ["user1", "user2", "user3"]


# Декоратор для перевірки, чи користувач зареєстрований
def user_registered(func):
    def verify(user, data):
        if registered_users.__contains__(user):
        
            return func(user, data)
        else: 
            return 'error'
    return verify



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