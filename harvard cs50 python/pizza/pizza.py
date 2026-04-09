import csv
import sys
from tabulate import tabulate

table = []

if len(sys.argv) != 2:
    sys.exit("Usage: python pizza.py FILENAME")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)

    # Use first row as headers
    headers = table[0]
    rows = table[1:]

    # tabulate with exact ASCII borders
    print(tabulate(rows, headers=headers, tablefmt="grid", stralign="left"))

except FileNotFoundError:
    sys.exit("File does not exist")
