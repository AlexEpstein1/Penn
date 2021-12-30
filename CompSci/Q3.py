def interleave(word1,word2):
	
	if len(word1) == 0:
		return word2

	if len(word2) == 0:
		return word1

	return word1[0] + word2[0] + interleave(word1[1:],word2[1:])


def main():
	word1 = input("Enter a word. ")
	word2 = input("Enter another word. ")
	print(interleave(word1,word2))

main()




