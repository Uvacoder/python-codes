def recursive_list_sum(list):
	total = 0
	for element in list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element

	return total

print(recursive_list_sum([1, 2, [3,4],[5,6]]))
