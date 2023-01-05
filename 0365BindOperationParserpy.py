import csv

with open('timelinetobreakout.csv', 'r') as input_csv:

  reader = csv.reader(input_csv)

  with open('brokenout.csv', 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)

    for row in reader:
      values = row[3]
      values = values.split('\n')

      for value in values:
        writer.writerow([row[0],row[1], row[2], value, row[4], row[5]])
