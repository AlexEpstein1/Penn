def rocket_top(n):
	for i in range(1,(2*n)):
		print((" " * ((2*n)-i)) + ("/" * i) + "**" + ("\\" * i))

def rocket_line(n):
	print("+" + ("=*" * (2*n)) + "+")

def rocket_body(n):
	for x in range(1,n):
		print( "|" + (((('.' * (n-x)) + ("/\\" * x) + ("." * (n-x))) * 2)) + "|")

def rocket_body2(n):
	for x in range(1,n):
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
