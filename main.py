from datetime import date, datetime


def get_birthdays_per_week(users):
    date_keys = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    mon = []
    tue = []
    wed = []
    thu = []
    fri = []
    result = {}

    def get_days_from_today(date):
        date_now = datetime.now()
        d1 = datetime(year=int(date_now.year), month=int(
            date.month), day=int(date.day))
        d0 = datetime(year=int(date_now.year), month=int(
            date_now.month), day=int(date_now.day))
        diferense = d1-d0
        res = diferense.days
        if res < -358:
            res = res + 365  # переход года
        return res

    def now_week(users):
        users_that_week = []
        now_day = datetime.now()
        for person in users:
            day = person['birthday']
            qw = get_days_from_today(day)
            new_day = datetime(year=int(now_day.year),
                               month=day.month, day=day.day)
            person['birthday'] = new_day
            if qw >= 0 and qw < 7:
                users_that_week.append(person)
        return users_that_week

    new_users = now_week(users)

    for person in new_users:
        day = person['birthday']
        day_week = day.weekday()
        if (day_week == 0):
            mon.append(person['name'])
        if (day_week == 1):
            tue.append(person['name'])
        if (day_week == 2):
            wed.append(person['name'])
        if (day_week == 3):
            thu.append(person['name'])
        if (day_week == 4):
            fri.append(person['name'])
        if (day_week == 5):
            mon.append(person['name'])
        if (day_week == 6):
            mon.append(person['name'])
    if mon != []:
        result[date_keys[0]] = mon
    if tue != []:
        result[date_keys[1]] = tue
    if wed != []:
        result[date_keys[2]] = wed
    if thu != []:
        result[date_keys[3]] = thu
    if fri != []:
        result[date_keys[4]] = fri
    users = result
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
