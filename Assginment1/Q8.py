days = int(input("Enter number of days: "))
years = days // 365
weeks = (days % 365) // 7
days_left = (days % 365) % 7
print(years, "Years", weeks, "Weeks", days_left, "Days")
