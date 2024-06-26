def add_time(start, duration, day_of_week = False):
    week_days_index = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_pm = start_minutes_tuple[2]
    am_pm_flip = {"AM":"PM", "PM":"AM"}
    amount_of_days = int(duration_hours / 24)

    end_minutes = start_minutes + duration_minutes

    if (end_minutes >= 60):
        start_hours += 1
        end_minutes = end_minutes % 60

    amount_am_pm_flips = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    if (am_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
        amount_of_days += 1

    am_pm = am_pm_flip[am_pm] if amount_am_pm_flips % 2 == 1 else am_pm

    end_time = str(end_hours) + ":" + str(end_minutes) + " " + am_pm

    if (day_of_week):
        day_of_week = day_of_week.lower()
        index = int((week_days_index[day_of_week]) + amount_of_days) % 7
        new_day = week_days[index]
        end_time += ", " + new_day

    if amount_of_days == 1:
        return end_time + " " + "(next day)"
    elif amount_of_days > 1:
        return end_time + " (" + str(amount_of_days) + " days later)"
    
    return end_time

print(add_time('2:59 AM', '24:00', 'saturDay'))