import re

def email_parse(email_address):
    result = re.match(r'.{3,}@\w+\.\w+', email_address)
    if result:
        return dict(zip(['adress', 'email'], result.group().split('@')))
    raise ValueError('не корректный адрес')

# email_parse(input('Введите свой email: '))

print(email_parse('asdsad@mail.ru'))
print(email_parse('asdsa912.213asad@mail.ru'))
print(email_parse('example@mail.group.net'))
