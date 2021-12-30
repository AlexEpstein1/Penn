#check if the isbnnumber is valid
def ISBN():
	code = input("Enter your ISBN code")

	d10 = (int(code[0]) * 1 + int(code[1]) * 2 + int(code[2]) * 3 + int(code[3]) * 4 + int(code[4]) * 5 + int(code[5]) * 6 + int(code[6]) *7 + int(code[7]) * 8 + int(code[8]) * 9) % 11

	if d10 == 10:
		if code[9]=='X':
			print("This code is valid")
		
		else:
			print("This code is not valid")
				

	elif d10 == int(code[9]):
			print("This code is valid")

	elif d10 != int(code[9]):
			print("This code is not valid. Expected " + str(d10) + ", but found " + code[9] )



def main():
	ISBN()

main()