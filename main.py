def month(schedule):
    '''Вывод таблицы расписания'''
    print('{:>10}'.format('| '),end = '')
    for i in range(1, 32):
        print(' {:^14} |'.format(str(i)+' декабря'), end = '')
    x = 9
    print('')
    for i in range(4):
        date = str(x)+':00'
        print('{:<8}| '.format(date), end = '')
        for i in range(31):
            if date in schedule[i]:
                print('{:^15} |'.format('занято'), end = '')
            else:
                print('{:^15} |'.format('свободно'), end = '')
        print('')
        x += 3
    print('')


def timetable(schedule):
    '''Бронирование времени'''
    try:
        day = int(input('Число: '))
        day_lst = int(day) - 1
        if len(schedule[day_lst]) < 4:
            print('{:>10}'.format('| '), end='')
            print(' {:^14} |'.format(str(day) + ' декабря'), end='')
            print('')
            x = 9
            for i in range(4):
                date = str(x) + ':00'
                print('{:<8}| '.format(date), end='')
                if date in schedule[day_lst]:
                    print('{:^15} |'.format('занято'), end='')
                else:
                    print('{:^15} |'.format('свободно'), end='')
                print('')
                x += 3
            time_lst = input('Выберите время(9/12/15/18): ')
            time = time_lst + ':00'
            if time in schedule[day_lst] or (
                    time_lst != '9' and time_lst != '12' and time_lst != '15' and time_lst != '18'):
                while True:
                    time_lst = input('На это время нельзя записаться, выберите другое время: ')
                    time = time_lst + ':00'
                    if time in schedule[day_lst] or (
                            time_lst != '9' and time_lst != '12' and time_lst != '15' and time_lst != '18'):
                        continue
                    else:
                        break
            schedule[day_lst].append(time)
            print('Время записано. ')
        else:
            print('В этот день нет свободного времени. Попробуйте другое. ')
            timetable(schedule)
    except ValueError:
        print('Число введено неправильно, введите число заново. ')
        timetable(schedule)



def main():
    print('{:^200}\n'.format('БРОНИРОВАНИЕ ВРЕМЕНИ ПОСЕЩЕНИЯ ТЕРАПЕВТА'))
    schedule = [[] for i in range(31)]
    while True:
        month(schedule)
        timetable(schedule)


if __name__ == '__main__':
    main()