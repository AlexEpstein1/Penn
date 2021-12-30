def factorial(n):
	#computes factorial of numbers>= 0
	if n == 1:
		return 1
	return n * factorial(n-1)

def main():
	print(factorial(4))

main()

def print_halves(n):
	if n <= 1:
		print("1")
	else:
		print_halves(n//2)
		print(n)

def main():
	print_halves(61)

main()

def print_even_digits_from_right(n):
	if n ==0:
		return
	
	elif n % 2 == 0:
		print_even_digits_from_right(n//10)
		print(n % 10)

	else:
		print_even_digits_from_right(n//10)

def main():
	print_even_digits_from_right(291875614)

main()

def print_even_digits_from_left(n):
	if n ==0:
		return
	
	elif n % 2 == 0:
		print(n % 10)
		print_even_digits_from_right(n//10)
		

	else:
		print_even_digits_from_right(n//10)

def main():
	print_even_digits_from_left(291875614)

main()

from __future__ import print_function
def print_sequence(n):
	if n == 1:
		print("1", end = '')
		return

	elif n ==2:
		print("1 1", end = '')
		return

	else:
		if n % 2!=0:
			high = n //2 +1
			
		else:
			high = n //2
		
		print(str(high) + " ", end = '')
		print_sequence(n-2)
		print(" " + str(high), end = '')

def main():
	for i in range(1,11):
		print_sequence(i)
		print("")

main()


