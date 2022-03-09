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