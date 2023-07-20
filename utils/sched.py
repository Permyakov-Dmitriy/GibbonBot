import schedule
import time


def timer_sched(sched, name, func, bot, id):
    sch = sched.split()
    format_sch = [i.split('/') if '/' in i else i.split() for i in sch]

    day = format_sch[0]
    HH_MM = format_sch[1]

    print(func)

    dict_day = {
        'пн': schedule.every().monday,
        'вт': schedule.every().tuesday,
        'ср': schedule.every().wednesday,
        'чт': schedule.every().thursday,
        'пт': schedule.every().friday,
        'сб': schedule.every().saturday,
        'вс': schedule.every().sunday,
    }

    for i in range(len(day)):
        dict_day[day[i]].at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)