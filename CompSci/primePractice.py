#check whether a number is prime or not
def prime(n):
	#check whether anything from 2 to n/2 divides n
	for factor in range(n//2 + 1):
		if factor >= 2:
			if n % factor == 0:
				return False
	return True


def main():
	sum_of_primes = 0
	#repeatedly check if numbers are prime
	for number in range(1,101):
		if prime(number):
			sum_of_primes += number
	print(sum_of_primes)


main()


