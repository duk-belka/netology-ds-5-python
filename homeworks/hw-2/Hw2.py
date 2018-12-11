# 1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def select_logs_from_country(logs, country):
    return [log for log in logs if country in list(log.values())[0]]


print('#1', select_logs_from_country(geo_logs, 'Россия'))

# 2

ids = {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]}

unique_id_list = []
for item in ids.values():
    unique_id_list += item

print('#2', sorted(unique_id_list))

# 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

search_word_count_info = {}
for query in queries:
    word_count = len(query.split(' '))
    if word_count in search_word_count_info:
        search_word_count_info[len(query.split(' '))] += 1
    else:
        search_word_count_info[len(query.split(' '))] = 1

queries_count = len(queries)

print('#3', {key: search_word_count_info[key] / queries_count for key in search_word_count_info.keys()})

# 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def get_key_with_max_value_form_dict(dictionary):
    max_value_key = None
    for key in dictionary.keys():
        if max_value_key not in dictionary.keys() or dictionary[max_value_key] < dictionary[key]:
            max_value_key = key
    return max_value_key


print('#4', get_key_with_max_value_form_dict(stats))

# 5

stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]
