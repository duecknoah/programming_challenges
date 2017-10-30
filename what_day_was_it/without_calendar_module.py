""" Challenge #338 [Easy] What day was it again?
https://www.reddit.com/r/dailyprogrammer/comments/79npf9/20171030_challenge_338_easy_what_day_was_it_again/

I used Zeller's algorithm to determine the day of month based off
the given date
"""
days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
date = input('Enter YYYY MM DD: ').split()

year = int(date[0])
month = int(date[1])
day = int(date[2])

if month == 1 or month == 2:
    month += 12
    year -= 1

year_str = str(year)
c = int(year_str[0] + year_str[1])
k = int(year_str[2] + year_str[3])

i = int(2.6 * month - 5.39)
i2 = int(k / 4)
i3 = int(c / 4)

sum = i + i2 + i3 + day + k - 2 * c

print('That date is on a {}'.format(days[sum % 7]))