import csv

with open("results_hola.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    rows = sum(1 for row in csv.reader(f))
    print(rows)
