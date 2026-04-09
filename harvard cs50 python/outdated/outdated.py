months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def check_day(day):
    return True if 1 <= int(day) <= 31 else False


while True:
    date = input("Date: ").strip()
    try:
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and check_day(day):
            print(f"{year}-{int(month):02}-{int(day):02}")
        else:
            continue
    except ValueError:
        continue
    try:
        month, day, year = date.split(" ")
        if month in months and check_day(day[0] and "," in day):
            print(f"{year}-{months.index(month)+1:02}-{int(day[0]):02}")
        else:
            continue
    except ValueError:
        continue
    break
