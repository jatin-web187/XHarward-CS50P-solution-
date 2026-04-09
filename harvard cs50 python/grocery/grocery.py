items_count = {}

# Read items until Ctrl+D (EOF)
while True:
    try:
        item = input().strip().lower()  # no prompt
        if item:  # ignore empty input
            if item in items_count:
                items_count[item] += 1
            else:
                items_count[item] = 1
    except EOFError:
        break

# Print sorted, uppercase grocery list
for item in sorted(items_count):
    print(f"{items_count[item]} {item.upper()}")
