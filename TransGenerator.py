class TransGenerator(object):

	def __init__(self, concurrency):
		self.concurrency = concurrency
		self.dates = ['2017-11-08']
		self.inputFile = open(self.concurrency + '/' + self.dates[0] + 'sort', 'r')
		self.inputSQL = self.inputFile.readlines()
		self.inputIndex = -1;

	def getNext(self):
		try:
			self.inputIndex += 1
			sql = self.inputSQL[self.inputIndex].strip('\n')
			if sql == '':
				return 'error'
			return sql
		except:
			if self.inputIndex >= len(self.inputSQL):
				self.inputFile.close()
			else:
				print('read error')
				return 'error'