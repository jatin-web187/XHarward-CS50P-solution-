import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match=re.findall(r"\bum\b",s,re.I)
    length=len(match)
    return length






if __name__ == "__main__":
    main()
