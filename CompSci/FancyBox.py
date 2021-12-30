def print_fancybox(n):
	for height in range(0,((2*n)-2)):
		if height < ((2*n)-2):
			print("|" + ("\\/" * 7) + "|")
	
def dashes(n):
	print("-" * 16)			
			

def main():
	n = int(input("Enter a height. "))
	dashes(n)
	print_fancybox(n)
	dashes(n)

main()