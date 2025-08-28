# There is no switch statement in python.
# We can use if-elif-else to implement switch case.
# Or we can use dictionary to implement switch case.

# Example of if-elif-else as switch case
# def week_day(day):
#     if day == 1:
#         return "Monday"
#     elif day == 2:
#         return "Tuesday"
#     elif day == 3:
#         return "Wednesday"
#     elif day == 4:
#         return "Thursday"
#     elif day == 5:
#         return "Friday"
#     elif day == 6:
#         return "Saturday"
#     elif day == 7:
#         return "Sunday"
#     else:
#         return "Invalid day"

# print(week_day(3))
# print(week_day(8))

# Example of dictionary as switch case
def week_day_dict(day):
    switcher = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switcher.get(day, "Invalid day")

print(week_day_dict(5))
print(week_day_dict(0))
