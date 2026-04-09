str_ =input ("Input:")
vowel=["A","E","I","O","U","a","e","i","o","u"]
temp=""
for ch in str_:
    if ch not in vowel:
        temp+=ch
print("output:",temp)


