import sys
import re

# with open(sys.argv[1]) as fin, open(sys.argv[2], 'a') as fout:
# 	date = sys.argv[2]
# 	for line in fin:
# 		if 'INSERT' in line:
# 			if date in line:
# 				fout.write(line)

# sort observation
# def timefilter(line):
# 	try:
# 		found = re.search('..:..:..', line).group(0)
# 	except AttributeError:
# 		print("Not Found!!!")
# 	return found

# with open(sys.argv[1]) as f:
# 	content = f.readlines()

# content = [x.rstrip('\n') for x in content]

# fsort = sorted(content, key = timefilter)
# fout = open(sys.argv[1] + 'sort', 'w+')
# for line in fsort:
# 	fout.write(line + '\n')
# fout.close()

# sort query
timestamps = []
queries = []
with open("queries.txt") as fin:
	content = fin.read()
	content_split = content.split('"')
	timestamps = content_split[0::2]
	timestamps = timestamps[0:-1]
	queries = content_split[1::2]

timestamps = [x.strip(',\n') for x in timestamps]
queries_sorted = [x for _,x in sorted(zip(timestamps, queries))]
timestamps.sort()
fout = open('queries_sorted.txt', 'w+')
for i, q in enumerate(queries_sorted):
	fout.write(timestamps[i] + '\n')
	fout.write(q.lstrip('\n'))
	fout.write('****')

fout.close()