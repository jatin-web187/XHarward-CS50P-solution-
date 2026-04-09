import random

while True:
    n = int(input("Level: "))
    if n <= 0:
        continue

    else:
        break
while True:
    try:
         guss=int(input("Guess "))
         if guss<=0:
                continue
         else:
                break

    except ValueError:
           pass
guss_num =random.randrange(1,n)
while True:
   try:
         if guss<guss_num:
            print("Too small!")
         elif guss>guss_num:
            print("Too large!")
         else:
            print("Just right!")
            break
   except ValueError:
            pass
