def main():
    s=input()
    print("Valid" if is_valid(s) else "Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    num_started = False
    for ch in s:
        if ch.isdigit():
            if not num_started:
                num_started = True
                if ch == '0':
                    return False
        else:
            if num_started:
                return False

    return True


if __name__ == "__main__":
    main()
