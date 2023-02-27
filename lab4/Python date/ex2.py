import datetime

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)

tomorrow = today + datetime.timedelta(days=1)

print("Today is:", today)
print("Yesterday was:", yesterday)
print("Tomorrow will be:",tomorrow)


