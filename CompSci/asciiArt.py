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

def rocket_top():
 	for i in range(1,6):
 		print((" " * (6-i)) + ("/" * i) + "**" + ("\\" * i))

def rocket_line():
	print("+" + ("=*" * 6) + "+")

def rocket_body():
 	for x in range(1,4):
 		print( "|" + (((('.' * (3-x)) + ("/\\" * x) + ("." * (3-x))) * 2)) + "|")

def rocket_body2():
 	for x in range(0,3):
 		print("|" + ((("." * x) + ("\\/" * (3-x)) + ("." * x)) * 2) + "|")

def main():
 	rocket_top()
 	rocket_line()
 	rocket_body()
 	rocket_body2()
 	rocket_line()
 	rocket_body2()
 	rocket_body()
 	rocket_line()
 	rocket_top()

 main()

def rocket_top(n):
	for i in range(1,(2*n)):
		print((" " * ((2*n)-i)) + ("/" * i) + "**" + ("\\" * i))

def rocket_line(n):
	print("+" + ("=*" * (2*n)) + "+")

def rocket_body(n):
	for x in range(1,n):
		print( "|" + (((('.' * (n-x)) + ("/\\" * x) + ("." * (n-x))) * 2)) + "|")

def rocket_body2(n):
	for x in range(0,n):
		print("|" + ((("." * x) + ("\\/" * (n-x)) + ("." * x)) * 2) + "|")

def main():
	n = int(input("How large would you like your rocket ship? "))
	rocket_top(n)
	rocket_line(n)
	rocket_body(n)
	rocket_body2(n)
	rocket_line(n)
	rocket_body2(n)
	rocket_body(n)
	rocket_line(n)
	rocket_top(n)

main()


