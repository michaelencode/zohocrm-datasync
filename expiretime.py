import time
from datetime import datetime

# Convert the given date and time to a Unix timestamp
given_datetime = datetime.strptime("2023-03-22 18:40", "%Y-%m-%d %H:%M")
given_timestamp = int(time.mktime(given_datetime.timetuple()))

# Add 15 days (15 * 24 * 60 * 60 seconds) to the Unix timestamp
expiry_time = given_timestamp + (15 * 24 * 60 * 60)
print(expiry_time)