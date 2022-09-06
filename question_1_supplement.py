import sys

if __name__=="__main__":
    '''This program I wrote up to work out the angles for the correct output for my test cases.
    There is no testing and that is fine.'''

    minutes = 0
    minutes_in_hour = 60
    hours = 0
    hours_in_half_day = 12
    hour_degrees = None
    min_degrees = None
    degrees_in_circle = 360

    time_string = sys.argv[1]

    time_denotation = time_string.split(' ')

    time_value = time_denotation[0]
    am_pm_value = time_denotation[1]
    hours_and_minutes = time_value.split(':')
    hours = hours_and_minutes[0]
    minutes = hours_and_minutes[1]
    print(minutes)
    print(hours)

    min_degrees = float(degrees_in_circle / minutes_in_hour) * float(minutes)
    hour_degrees = float(degrees_in_circle / hours_in_half_day) * float(hours)
    print(f"{hour_degrees} - {min_degrees} = {hour_degrees-min_degrees}")
