user_time = int(input("Введите количество секунд: "))

if (user_time > 0 and user_time < 60):
    print(f'{user_time} секунд')
elif (user_time >= 60 and user_time < 3600):
    user_min = user_time // 60
    user_sek = user_time % 60
    print(f'{user_min} минут(ы), {user_sek} секунд')
elif (user_time >= 3600 and user_time < 86400):
    user_hour = user_time // 3600
    user_min = (user_time % 3600) // 60
    user_sek = (user_time % 3600) % 60
    print(f'{user_hour} час(ов), {user_min} минут(ы), {user_sek} секунд')
elif (user_time >= 86400):
    user_days = user_time // 86400
    user_hour = (user_time % 86400) // 3600
    user_min = (user_time % 3600) // 60
    user_sek = (user_time % 3600) % 60
    print(f'{user_days} дней, {user_hour} час(ов), {user_min} минут(ы), {user_sek} секунд')
else:
    print("Введено некорректное число секунд")
