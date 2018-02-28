def simple_firstn(n):
	num, nums = 0, []
	while num < n:
		nums.append(num)
		num += 1
	return nums

sum_of_firstn = sum(simple_firstn(1000000))