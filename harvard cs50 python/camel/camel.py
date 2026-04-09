camelCase = input("camelCase: ")
snake_case = ""

for i in range(len(camelCase)):
    if camelCase[i].isupper():
        if i != 0:  # avoid underscore at start
            snake_case += "_"
        snake_case += camelCase[i].lower()
    else:
        snake_case += camelCase[i]

print("snake_case:", snake_case)


# check if letter is uppercase


# print underscore and the letter  is lowercase


# otherwise print    letter



# print space in the end
