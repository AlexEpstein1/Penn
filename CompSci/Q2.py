def sum_digits(num):
	if num % 10 == num:
		return num

	else:
		return (num % 10) + (sum_digits(num // 10))



def main():
	num = int(input("Enter a number. "))
	print(sum_digits(num))

main()
