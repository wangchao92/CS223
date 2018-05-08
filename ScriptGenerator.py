import os

inputFiles = []
date = ['2017-11-09', '2017-11-08', '2017-11-10', '2017-11-11', '2017-11-12', '2017-11-13', '2017-11-14', '2017-11-15', '2017-11-16', '2017-11-17', '2017-11-18', '2017-11-19', '2017-11-20', '2017-11-21', '2017-11-22', '2017-11-23', '2017-11-24', '2017-11-25', '2017-11-26', '2017-11-27', '2017-11-28']

# for root, dirs, files in os.walk("."):  
#     for filename in files:
#     	if 'xa' in filename or 'xb' in filename:
#     		inputFiles.append(filename)

# with open('splitscript.sh', 'w+') as script:
# 	for fin in inputFiles:
# 		for dat in date:
# 			script.write('python Preprocessor.py ' + fin + ' ' + dat + '\n')

with open('sortscript.sh', 'w+') as script:
	for dat in date:
		script.write('python Preprocessor.py ' + dat + '\n')