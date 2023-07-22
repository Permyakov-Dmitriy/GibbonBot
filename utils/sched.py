import schedule
import time


def format_for_sched(sched):
    sch = sched.split()
    format_sch = [i.split('/') if '/' in i else i.split() for i in sch]

    day = format_sch[0]
    HH_MM = format_sch[1]

    return (day, HH_MM)


def timer_sched(sched, name, func, bot, id_grp, format=None):
    if format == None:
        format = format_for_sched(sched)

    elif not format[0]:
        return

    dict_day = {
        'пн': schedule.every().monday,
        'вт': schedule.every().tuesday,
        'ср': schedule.every().wednesday,
        'чт': schedule.every().thursday,
        'пт': schedule.every().friday,
        'сб': schedule.every().saturday,
        'вс': schedule.every().sunday,
    }

    dict_day[format[0][0]].at(format[1][0]).do(lambda: func(bot, id_grp, name)).tag(f"timer_{name}")

    timer_sched(sched, name, func, bot, id_grp, [i[1:] for i in format])


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)