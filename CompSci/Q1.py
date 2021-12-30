def count_x(word):
	if len(word) == 0:
		return 0
	if len(word) == 1:
		if word == 'x':
			return 1
		else:
			return 0
	#recursive part
	smaller_string = count_x(word[1:])
	if word[0] == 'x':
		return 1 + smaller_string
	else:
		return smaller_string


def main():
	word = input("Enter a word. ")
	print(count_x(word))
	
main()