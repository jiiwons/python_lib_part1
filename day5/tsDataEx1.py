from datetime import datetime

now = datetime.now()
print(now)
print('{}년 {}월 {}일'.format(now.year, now.month, now.day))
print()

time1 = datetime(2015, 2, 22, 10, 20)
print(time1)
print(time1.strftime('%Y-%m-%d'))
print()

timestr = '2020-01-07'
time2 = datetime.strptime(timestr, '%Y-%m-%d')
print(time2)


from dateutil.parser import parse
print()
print(parse('2020-01-07'))
print(parse('Jan 31, 2020 10:45 PM'))
