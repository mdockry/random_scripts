import csv

with open('timeline.csv', 'r') as file:
  reader = csv.reader(file)
  rows = list(reader)

column_d_index = rows[0].index('InternetMessageId')
column_a_index = rows[0].index('Time')

unique_values = set(row[column_d_index] for row in rows[1:])

with open('timeline.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['InternetMessageId', 'Matching Times'])

  print(unique_values)

  for value in unique_values:
    matching_times = [row[column_a_index] for row in rows[1:] if row[column_d_index] == value]
    writer.writerow([value,', '.join(matching_times)])
