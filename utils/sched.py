import schedule
import time


def timer_sched(sched, name, func, bot, id):
    sch = sched.split()
    format_sch = [i.split('/') if '/' in i else i.split() for i in sch]

    day = format_sch[0]
    HH_MM = format_sch[1]

    for i in range(len(day)):
        match day[i]:
            case "пн":
                schedule.every().monday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")
            case "вт":
                schedule.every().tuesday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")
            case "ср":
                schedule.every().wednesday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")
            case "чт":
                schedule.every().thursday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")
            case "пт":
                schedule.every().friday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")
            case "сб":
                schedule.every().saturday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")
            case "вс":
                schedule.every().sunday.at(HH_MM[i]).do(lambda: func(bot, id)).tag(f"timer{name}")


def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)