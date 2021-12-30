from functools import*

def ones_digit(l):
	return [x % 10 for x in l]

def lengths_of(l):
	return [len(x) for x in l]

def filter_odd_lengths(l):
	return [x for x in l if len(x) % 2 !=0]

def filter_upper(l):
	return [x for x in l if x.isupper()]

def list_all(l):
	if len(l) == 0:
		return False
	else:
		return reduce(lambda x, y: x and y, l)

def list_any(l):
	if len(l) == 0:
		return False
	else:
		return reduce(lambda x, y: x or y, l)
	
def immutable_replicate(l, n):
 	return l * n

def mutable_replicate(l, n):
	l *= n

def at_least(l,s,n):
	lst = list(filter(lambda x: x== s, l))
	if len(lst) >= n:
		return True
	else:
		return False


def main():
	print(ones_digit([123,12,33]))
	print(lengths_of(["123","12","33"]))
	print(filter_odd_lengths(["123","12","33"]))
	print(filter_upper(['AA', 'bb', 'CC', 'Ab']))
	print(list_all([True, False, True]))
	print(list_any([]))
	print(immutable_replicate([1,2,3], 3))
	
	list1= [1,2,3]
	mutable_replicate(list1, 3)
	print(list1)


	print(at_least([3,3,4,1,3],3,3))

main()

