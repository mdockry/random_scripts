import datetime
import string
import re 
pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d\.')
epoch_times=[]

#open audit.log file, read contents, find regex hits, export to list, clean up list and cast str to int for time conversion

with open('audit.log', 'r', encoding='utf-8') as f:
	for line in f:
		match = pattern.findall(line)
		if match:
			new = ', '.join(match)
			new_string = new.translate(str.maketrans('', '', string.punctuation))
			epoch_times.append(new_string)

clean_epoch_times = (list(map(int, epoch_times)))


for time in clean_epoch_times:
    timestamp = datetime.datetime.fromtimestamp(time)
    print(timestamp)




