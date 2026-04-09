import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, "r") as infile:
        reader = csv.DictReader(infile)

        with open(output_file, "w", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first","last","house"])
            writer.writeheader()

            for row in reader:
                # Split last, first from name column
                last, first = [part.strip() for part in row["name"].split(",")]
                writer.writerow({"first": first, "last": last, "house": row["house"].strip()})

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")
