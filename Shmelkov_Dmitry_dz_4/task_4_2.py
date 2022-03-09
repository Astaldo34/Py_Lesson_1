from requests import get
response = get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates (code):
    str_currency = response.text[response.text.find(code):]
    str_value = str_currency[str_currency.find('Value') + 6:]
    cur_price = ''
    for value in str_value:
        if value == '<':
            break
        cur_price += value
    return print(cur_price)


currency_rates('AMD')
# print(response.text)
# print(response.text.find('AUD'))
# str_currency = response.text[response.text.find('AUD'):]
# print(str_currency)
# print(str_currency.find('Value'))
# print(str_currency[str_currency.find('Value') + 6:])
# str_value = str_currency[str_currency.find('Value') + 6:]
# cur_price = ''
# for value in str_value:
#     if value == '<':
#         print(value)
#         break
#     cur_price += value
#
#
# print(cur_price)




