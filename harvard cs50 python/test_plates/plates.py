def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. Length check
    if len(s) < 2 or len(s) > 6:
        return False

    # 2. Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # 3. Only letters and numbers allowed
    if not s.isalnum():
        return False

    # 4. Numbers must come only at the end
    num_started = False
    for ch in s:
        if ch.isdigit():
            if not num_started:
                num_started = True
                # first number cannot be '0'
                if ch == '0':
                    return False
        else:
            if num_started:
                return False

    return True

if __name__=="_main_":
    main()

