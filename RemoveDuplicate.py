lines_seen = set()
with open("low/2017-11-08sort") as fin:
	with open("low/2017-11-08sort2", 'w+') as fout:
		for line in fin:
			if line not in lines_seen:
				lines_seen.add(line)
				fout.write(line)