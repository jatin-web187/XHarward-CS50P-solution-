import re

def validate(ip):
    # Match 4 numeric parts
    if not re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        return False

    parts = ip.split(".")
    for part in parts:
        # Reject leading zeros (except "0")
        if len(part) > 1 and part.startswith("0"):
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True

def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))

if __name__ == "__main__":
    main()
