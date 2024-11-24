import calendar
from datetime import datetime

# Get the current date
today = datetime.now()

# Extract current month and year
current_year = today.year
current_month = today.month

# Generate the calendar
print(calendar.month(current_year, current_month))
