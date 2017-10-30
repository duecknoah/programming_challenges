""" Challenge #338 [Easy] What day was it again?
https://www.reddit.com/r/dailyprogrammer/comments/79npf9/20171030_challenge_338_easy_what_day_was_it_again/
"""
import calendar as cal

date = input('Enter YYYY MM DD: ').split()

year = int(date[0])
month = int(date[1])
day = int(date[2])

print(cal.day_name[cal.weekday(year, month, day)])