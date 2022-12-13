# Excercise of If else
# import time
# timeStamp = time.localtime()
# print(timeStamp)

# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

import time

t = time.localtime()
current_time = int(time.strftime("%H", t))
print(current_time)

if (current_time <= 6):
    print("Good Night!")
elif (current_time > 6 and current_time <= 12):
    print("Good Morning!")
elif (current_time > 12 and current_time <= 18):
    print("Good Afternoon!")
else:
    print("Good Night")
