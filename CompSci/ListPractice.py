def cube(x):
	return x ** 3

def is_even(x):
	return x%2 == 0

list1 = [1, 2, 3]
#map function
#first argument - name of a function
print(list(map(cube, list1)))
#uses cube function on every element of the list

#lambda function for cube
print(list(map(lambda x: x ** 3, list1)))

#filter function
#needs a function that returns a boolean
print(list(filter(is_even, list1)))

#same thing but creates it as new list
list_of_evens = list(filter(is_even, list1))
list_of_evens = list(filter(lambda x: x % 2 == 0, list1))
print(list_of_evens)


#Common super useful reductions
import functools

functools.reduce(lambda x,y: x+y,list1)
functools.reduce(lambda x,y: x*y,list1)