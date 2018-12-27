from datetime import datetime, timedelta
import calendar


def date_range(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    for i in range((end_date - start_date).days):
        yield start_date + timedelta(days=i)


start = '2018-12-10'
end = '2018-12-20'

print('#1', list(date_range(start_date=start, end_date=end)))


def date_range_with_validation(start_date, end_date):
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        yield

    if start_date > end_date:
        yield

    for i in range((end_date - start_date).days):
        yield start_date + timedelta(days=i)


start = '2018-12-20'
end = '2018-12-10'

print('#2', list(date_range_with_validation(start_date=start, end_date=end)))


def is_date_valid(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True


stream = ['2018-04-02', '2018-02-29', '2018-19-02']

print('#3', list(is_date_valid(i) for i in stream))


def current_month_date_list():
    today = datetime.today()

    if today.day == 1:
        start_date = (today - timedelta(days=1)).replace(day=1)
    else:
        start_date = today.replace(day=1)

    for i in range((today - start_date).days):
        yield (start_date + timedelta(days=i)).strftime('%Y-%m-%d')


print('#4', list(current_month_date_list()))


def hi_siri(command):
    today = datetime.today()
    if command == 'today':
        date = today
    elif command == 'last monday':
        date = today - timedelta(today.weekday())
    elif command == 'last day':
        m_range = calendar.monthrange(today.year, today.month)
        date = today.replace(day=m_range[1])
    else:
        return None

    return date.strftime('%Y-%m-%d')


print('#5', hi_siri('today'))
print('#5', hi_siri('last monday'))
print('#5', hi_siri('last day'))


def get_weeks(start_date, end_date):
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    weeks = list()

    for i in range((end_date - start_date).days):
        date = start_date + timedelta(days=i)
        if date.weekday() == 0 and (date + timedelta(days=7)) <= end_date:
            week = list()
            for i in range(7):
                week.append((date + timedelta(days=i)).strftime('%Y-%m-%d'))
            weeks.append(week)
    return weeks


print('#6', get_weeks('2018-12-01', '2018-12-25'))
