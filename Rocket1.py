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