def main():
    str_ =input ("Input:")
    print(shorten(str_))

def shorten(str_):

    vowel=["A","E","I","O","U","a","e","i","o","u"]
    temp=""
    for ch in str_:
        if ch not in vowel:
            temp+=ch
    return temp



if __name__ == "__main__":
    main()
