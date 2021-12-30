def alphabetical(word1,word2):
	
	if len(word1) == 0:
		return word2

	if len(word2) == 0:
		return word1

	elif word1[0]>word2[0]:

		return word2[0] + alphabetical(word1,word2[1:])
	
	elif word1[0]<word2[0]:
	
		return word1[0] + alphabetical(word1[1:],word2)

	elif word1[0]==word2[0]:

		return word1[0] + word2[0] + alphabetical(word1[1:],word2[1:])



def main():
	word1 = input("Enter a word. ")
	word2 = input("Enter another word. ")
	print(alphabetical(word1,word2))

main()
