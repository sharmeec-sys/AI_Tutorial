from datetime import datetime, date, timedelta

# 1. Get current date and time
current_datetime = datetime.now()
print("Current Date & Time:", current_datetime)

# 2. Format date and time
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted_datetime)

# 3. Extract date components
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)

# 4. Working with date only
today_date = date.today()
print("\nToday's Date:", today_date)

# 5. Add and subtract days using timedelta
future_date = today_date + timedelta(days=10)
past_date = today_date - timedelta(days=5)

print("Date after 10 days:", future_date)
print("Date before 5 days:", past_date)

# 6. Difference between two dates
date1 = date(2025, 1, 1)
date2 = date(2025, 12, 31)
difference = date2 - date1

print("\nDifference between dates:", difference.days, "days")
