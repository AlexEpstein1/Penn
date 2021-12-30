def duplicates(word):
	if len(word) <= 1:
		return word
	
	elif word[0] != word[1]:
		return word[0] + duplicates(word[1:])

	elif word[0] == word[1]:
		return word[0] + duplicates(word[2:])



def main():
	word = input("Enter a word. ")
	print(duplicates(word))


main()