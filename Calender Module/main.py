
import calendar
import datetime
def demonstrate_calendar_functions():
    print("=== Calendar Module Functions Demo ===\n")
    
    # Basic calendar display
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))
    
    print(f"\n1. Monthly Calendar for {month}/{year}:")
    calendar_text = calendar.month(year, month)
    print(calendar_text)
    
    # Text calendar for entire year
    print(f"\n2. Text Calendar for entire year {year}:")
    year_calendar = calendar.calendar(year)
    print(year_calendar)
    
    # Day of week functions
    print("\n4. Day of Week Information:")
    print(f"First day of week: {calendar.firstweekday()}")
    print(f"Day names: {list(calendar.day_name)}")
    print(f"Abbreviated day names: {list(calendar.day_abbr)}")
    print(f"Month names: {list(calendar.month_name)}")
    print(f"Abbreviated month names: {list(calendar.month_abbr)}")
    
    # What day of week is a specific date?
    print(f"\n5. What day is the 15th of {month}/{year}?")
    day_of_week = calendar.weekday(year, month, 15)
    print(f"Day number: {day_of_week} ({calendar.day_name[day_of_week]})")
    
    # Is it a leap year?
    print(f"\n6. Leap Year Check:")
    print(f"Is {year} a leap year? {calendar.isleap(year)}")
    print(f"Leap years between 2020-2030: {calendar.leapdays(2020, 2030)}")
    
    # Month range - first weekday and number of days
    print(f"\n7. Month Range for {month}/{year}:")
    first_weekday, num_days = calendar.monthrange(year, month)
    print(f"First day of month falls on: {calendar.day_name[first_weekday]}")
    print(f"Number of days in month: {num_days}")
    
    # Month calendar as lists
    print(f"\n8. Month as nested lists:")
    month_calendar = calendar.monthcalendar(year, month)
    for week in month_calendar:
        print(week)
    
    # Time-based calendar
    print(f"\n9. Time-based calendar functions:")
    now = datetime.datetime.now()
    print(f"Current time: {now}")
    print(f"Time to calendar: {calendar.timegm(now.timetuple())}")
    
    # Different calendar types
    print(f"\n10. Different Calendar Systems:")
    
    # Text calendar with different first day
    print("Calendar with Monday as first day:")
    calendar.setfirstweekday(calendar.MONDAY)
    print(calendar.month(year, month))
    
    print("Calendar with Sunday as first day:")
    calendar.setfirstweekday(calendar.SUNDAY)
    print(calendar.month(year, month))
    
    # Local calendar
    print(f"\n11. Locale-aware calendar:")
    try:
        local_cal = calendar.LocaleTextCalendar()
        print(local_cal.formatmonth(year, month))
    except:
        print("Locale calendar not available")
    
    # Different formatting options
    print(f"\n12. Different formatting widths:")
    print("Width 2:")
    print(calendar.month(year, month, w=2))
    print("Width 4:")
    print(calendar.month(year, month, w=4))
    
    # Iterators
    print(f"\n13. Calendar Iterators:")
    print("Weekdays iterator:")
    for i, day in enumerate(calendar.Calendar().iterweekdays()):
        if i < 7:  # Show first week only
            print(f"Day {i}: {calendar.day_name[day]}")
    
    print(f"\nMonth days iterator for {month}/{year}:")
    cal = calendar.Calendar()
    month_days = list(cal.itermonthdates(year, month))
    print(f"First few dates: {month_days[:7]}")
    
    # PRN (pretty print) functions
    print(f"\n14. Pretty Print Functions:")
    print("Pretty print month:")
    calendar.prmonth(year, month)
    
    print(f"\n15. Week header:")
    print(calendar.weekheader(3))  # 3-character week header

if __name__ == '__main__':
    demonstrate_calendar_functions()
