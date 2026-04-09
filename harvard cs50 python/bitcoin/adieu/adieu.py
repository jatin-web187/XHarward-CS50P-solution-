import inflect

p = inflect.engine()
names = []

try:
    while True:
        name = input("Name: ")
        names.append(name)
except EOFError:
    print()

# Use inflect to format list
formatted_names = p.join(names)

print(f"Adieu, adieu, to {formatted_names}")
