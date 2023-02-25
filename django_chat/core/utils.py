def is_room_existing(room_name, chat_room):
    return room_name in [room.room_name for room in chat_room.objects.all()]


def format_date(date_elements):
    months = {
        '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec',
    }
    time_to_pm = {
        '13': '1',
        '14': '2',
        '15': '3',
        '16': '4',
        '17': '5',
        '18': '6',
        '19': '7',
        '20': '8',
        '21': '9',
        '22': '10',
        '23': '11'
    }
    date = date_elements[0]
    time = date_elements[1].split('.')[0].split(':')

    date_elements = date.split('-')
    result = months[date_elements[1]] + '. ' + date_elements[2] + ', ' + date_elements[0] + ', ' + \
             time_to_pm[time[0]] + f':{time[1]} p.m.'

    return result
