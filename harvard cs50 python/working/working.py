import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$",s, re.I)

    if time:
        time_parts = list(time.groups())

        if time_parts[1] == None:
            time_parts[1] = 0

        if time_parts[4] == None:
            time_parts[4] = 0

        if int(time_parts[0]) > 12 or int(time_parts[3]) > 12:
            raise ValueError

        if int(time_parts[1]) > 59 or int(time_parts[4]) > 59:
            raise ValueError

        lhs_time = convert_hour(time_parts[0],time_parts[1],time_parts[2])
        rhs_time = convert_hour(time_parts[3],time_parts[4],time_parts[5])

        return lhs_time + " to " + rhs_time
    else:
        raise ValueError

def convert_hour(hh,mm,xx):
    if xx == "PM":
        if int(hh) == 12:
            new_hh = 12
        else:
            new_hh = int(hh) + 12
    else:
        if int(hh) == 12:
            new_hh = 0
        else:
            new_hh = int(hh)

    new_time = (f"{new_hh:02}") + ":" + (f"{mm:02}")
    return new_time

if __name__ == "__main__":
    main()