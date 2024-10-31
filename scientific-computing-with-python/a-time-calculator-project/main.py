def add_time(start, duration, dayOfWeek=''):
    if dayOfWeek:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday',
                        'Thursday', 'Friday', 'Saturday', 'Sunday']
        days_of_week_lower = [item.lower() for item in days_of_week]
        days_of_week_index = days_of_week_lower.index(dayOfWeek.lower())

    index_of_mid = start.find(':')
    start_hour = start[:index_of_mid]
    start_time = start[index_of_mid + 1:index_of_mid + 3]
    clock_format = start[-2:]

    index_of_mid = duration.find(':')
    duration_hour = duration[:index_of_mid]
    duration_time = duration[index_of_mid + 1:index_of_mid + 3]

    days_later = 0

    plus_an_hour = 0
    new_time_minute = int(start_time) + int(duration_time)
    if new_time_minute >= 60:
        new_time_minute = new_time_minute % 60
        plus_an_hour += 1

    new_time_hour = int(start_hour) + int(duration_hour) + plus_an_hour
    while new_time_hour > 12:
        if clock_format == 'PM':
            clock_format = 'AM'
            days_later += 1
        elif clock_format == 'AM':
            clock_format = 'PM'
        new_time_hour -= 12

    if new_time_hour == 12:
        if clock_format == 'PM':
            clock_format = 'AM'
            days_later += 1
        elif clock_format == 'AM':
            clock_format = 'PM'

    new_time = f'{new_time_hour}:{new_time_minute:02d} {clock_format}'

    if dayOfWeek:
        days_of_week_index = (days_of_week_index + days_later) % 7
        new_time += f', {days_of_week[days_of_week_index]}'

    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 0:
        new_time += f' ({days_later} days later)'

    return new_time


if __name__ == '__main__':
    print(add_time('3:00 PM', '3:10'))
    # Returns: 6:10 PM

    print(add_time('11:30 AM', '2:32', 'Monday'))
    # Returns: 2:02 PM, Monday

    print(add_time('11:43 AM', '00:20'))
    # Returns: 12:03 PM

    print(add_time('10:10 PM', '3:30'))
    # Returns: 1:40 AM (next day)

    print(add_time('11:43 PM', '24:20', 'tueSday'))
    # Returns: 12:03 AM, Thursday (2 days later)

    print(add_time('6:30 PM', '205:12'))
    # Returns: 7:42 AM (9 days later)
