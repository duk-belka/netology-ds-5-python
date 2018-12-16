import requests


def get_most_expensive_currency():
    currency_list = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']
    max_currency = None
    for currency_name in currency_list:
        if max_currency is None:
            max_currency = currency_list[currency_name]
        else:
            if max_currency['Value'] < currency_list[currency_name]['Value']:
                max_currency = currency_list[currency_name]
    return max_currency


print(get_most_expensive_currency()['Name'])
