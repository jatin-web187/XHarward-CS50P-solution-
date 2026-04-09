def main():
    loop=True
    while loop:
        try:
            fraction=input("fraction")
            percentage= convert(fraction)
            result=gauge(percentage)
            loop =False
            print(result)
        except (ValueError, ZeroDivisionError):
             pass



def convert(fraction):
    x, y = fraction.split("/")
    x=int(x)
    y=int(y)
    percent=x/y
    if percent>1:
        main()
    else:
        percent=percent*100
        percent=round(percent)
        return percent


def gauge(percentage):
    if percentage <= 1:
            return "E"

    elif percentage >= 99:
            return "F"
    else:
            return f"{percentage}%"

if __name__ == "__main__":
    main()
