"""
$ python3 csv_file.py
"""

import csv
import os

# CSV file
filename = 'csv/csv_sample.csv'

# check if the file is empty
if os.stat(filename).st_size == 0:
    print("File is empty")

# write to CSV
print("Writing on CSV...")
data = ["first_name,last_name,city".split(","),
        "Tyrese,Hirthe,Strackeport".split(","),
        "Jules,Dicki,Lake Nickolasville".split(","),
        "Dedric,Medhurst,Stiedemannberg".split(",")
        ]
csv_file = open(filename, 'a')  # appending mode
writer = csv.writer(csv_file, delimiter=',')

max_rows = 10
for line in data:
    i = 0
    while i < max_rows:
        writer.writerow(line)
        i += 1

# read CSV
print("Reading CSV...")
csv_file = open(filename, 'r')  # read mode
reader = csv.reader(csv_file)

for row in reader:
    print(" ".join(row))

# Truncate the file
print("Truncating the file...")
f = open(filename, "w")
f.truncate()
f.close()
