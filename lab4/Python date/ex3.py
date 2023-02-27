import datetime

today_with_ms = datetime.datetime.now()
today_without_ms = today_with_ms.replace(microsecond = 0)


print("Data with microseconds:", today_with_ms)
print("Data without microseconds:", today_without_ms)

