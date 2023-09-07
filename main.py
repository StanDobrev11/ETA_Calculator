"""
INPUT               OUTPUT
07-09-23 12-00
9
-6
7001
1
19.5
                    2023-09-21 20:00:00 LT
                    2023-09-22 02:00:00 UTC

07-09-23 12-00
9
-6
7001
2
21-09-23 20-00
                    Required speed: 19.5kn

07-09-23 12-00
-6
9
7001
1
19.5
                    2023-09-23 02:00:00 LT
                    2023-09-22 17:00:00 UTC

07-09-23 12-00
-6
9
7001
2
23-09-23 02-00
                    Required speed: 19.5 kn
"""

from datetime import datetime, timedelta

dep_date_time_lt = (datetime.strptime
                    (input('Enter departure date/time in format (DDMMYY HHMM): '), '%d%m%y %H%M'))
dep_port_utc_offset = timedelta(hours=float(input('Enter departure port difference to UTC (LT = UTC +/-): ')))
arr_port_utc_offset = timedelta(hours=float(input('Enter arrival port difference to UTC (LT = UTC +/-): ')))

dep_date_time_utc = dep_date_time_lt - dep_port_utc_offset
distance = int(input('Input distance in NM: '))

task_chosen = input('Calculated ETA(1) or calculated required SOG(2)?: ')

if task_chosen == '1':
    speed = float(input('Enter SOG in kn: '))
    travel_time = timedelta(hours=round(distance / speed, 1))
    arr_date_time_utc = dep_date_time_utc + travel_time
    arr_date_time_lt = arr_date_time_utc + arr_port_utc_offset
    print(arr_date_time_lt, 'LT')
    print(arr_date_time_utc, 'UTC')
else:
    arr_date_time_lt = (datetime.strptime
                        (input('Enter arrival date/time in format (DDMMYY HHMM): '), '%d%m%y %H%M'))
    arr_date_time_utc = arr_date_time_lt - arr_port_utc_offset
    travel_time = arr_date_time_utc - dep_date_time_utc
    days, seconds = travel_time.days, travel_time.seconds
    travel_time = days * 24 + seconds / 3600
    speed = round(distance / travel_time, 1)
    print(f'Required speed: {speed} kn')
