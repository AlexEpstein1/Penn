#check if the isbn number is valid
def ISBN():
	code = input("Enter your ISBN code ")

	d10 = 0
	for i in range (0,9):
		d10+= ((int(code[i]) * (i+1))) 

		final = d10 % 11

	if final == 10:
		if code[9]=='X':
			print("This code is valid")
		
		else:
			print("This code is not valid")
				

	elif final == int(code[9]):
			print("This code is valid")

	elif final != int(code[9]):
			print("This code is not valid. Expected " + str(final) + ", but found " + code[9] )



def main():
	ISBN()

main()