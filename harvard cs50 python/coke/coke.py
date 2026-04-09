cent = 50

while cent > 0:
    print("Amount Due:",cent)
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
        cent -= coin
    # invalid coins are ignored

# when loop ends, amount_due <= 0
print("Change Owed:", abs(cent))


