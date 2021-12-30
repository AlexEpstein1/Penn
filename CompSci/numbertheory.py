def sum_of_factors(n):
	end_sum = 0
	for number in range(1,(n-1)):
		if n % number == 0:
			end_sum += number
	return end_sum

def sum_of_digits(n, p):
	total = 0
	for i in range(len(n)):
		total+= int(n[i]) ** p
	return total	


def prime(n):
	for factor in range(n//2 + 1):
		if factor >= 2:
			if n % factor == 0:
				print(str(n)+ " is not a prime number")
				return
	print(str(n)+ " is a prime number")

def perfect(n):
	final = sum_of_factors(n)
	if final == n:
		print(str(n) + " is a perfect number")

	else:
		print(str(n) + " is not a perfect number")

def abundant(n):
	final = sum_of_factors(n) 
	if final > n:
		print(str(n) + " is an abundant number")

	else:
		print(str(n) + " is not an abundant number")

def narcissistic(n):
	final = sum_of_digits(n, len(n))
	if final == int(n):
			print(n + " is a narcissistic number")

	else:
			print(n + " is not a narcissistic number")

def harshad(n):
	final = sum_of_digits(n, 1)
	
	if int(n) % final == 0:
		print(n + " is a harshad number")
	else:
		print(n + " is not a harshad number")

def main():
	n = input("Choose a number. ")
	prime(int(n))
	perfect(int(n))
	abundant(int(n))
	narcissistic(n)
	harshad(n)

main()

			