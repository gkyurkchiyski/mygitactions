import datetime

target_datetime = datetime.datetime(2020, 1, 2, 12, 39, 1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")
