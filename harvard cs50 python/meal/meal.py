def main():
    time_str = input("please enter time")
    time_flot= convert(time_str)
    if 7.0<= time_flot<=8.0:
        print("breakfast time")
    elif 12.0<=time_flot<=13.0:
        print("lunch time")
    elif 18.0 <= time_flot <= 19.0:
        print("dinner time")


def convert(time):
    # Split the string by ':' to separate hours and minutes
    hours_str, minutes_str = time.split(":")

    # Convert both to floats
    hours = float(hours_str)
    minutes = float(minutes_str)

    # Return total hours as a float
    return hours + (minutes / 60.0)

if __name__ =="__main__":
    main()
