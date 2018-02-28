def simple_firstn(n):
	num, nums = 0, []
	while num < n:
		nums.append(num)
		num += 1
	return nums

# using the generator pattern
class firstn(object):

	def __init__(self, n):
		self.n = n;
		self.num, self.nums = 0, []

	def __iter__(self):
		return self

	def __next__(self):
		return self.next()

	def next(self):
		if self.num < self.n:
			cur, self.num = self.num, self.num+1
			return cur
		else:
			raise StopIteration()