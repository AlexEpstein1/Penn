def print_pyramid(n):
	for i in range (0,n):
		if i < n:
			print((" " * (n-i)) + "/" + ("*=" * i) + "\\")

def dashes(n):
	print(" " + "-" * (n * 2))	

def main():
	n = int(input("Enter a height. "))
	print_pyramid(n)
	dashes(n)

main()
