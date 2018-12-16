request = [
    ['2018-01-01', 'yandex', 'cpc', 100],
    ['2018-01-02', 'yandex', 'cpc', 200],
    ['2018-01-03', 'yandex', 'cpc', 300],
    ['2018-01-04', 'yandex', 'cpc', 400],
]


def translate_request_to_dict(request):
    return {item[0]: {item[1]: {item[2]: item[3]}} for item in request}
