def girl_named_fred():
	print("I'm in love with a girl named Fred.")

def spell_fred():
	print('With a "F" and a "R" and an "E" and a "D"\nAnd a "F-R-E-D" Fred!  Yeah!\n')

def fill_the_bowl():
	print("Fill the bowl to overflowing.  Raise the goblet high!")
	spell_fred()

def la_la():
	print("La la la la, la la la la, la la la la la!")
	fill_the_bowl()

def clap():
	print("Clap clap, clap clap, clap clap clap clap, clap, clap clap!")
	la_la()

def bravo():
	print("Bravo!  Bravo!  Bravissimo bravo!  Bravissimo!")
	clap()

def strum():
	print("Strum strum, strum strum, strum strum strum strum strum, strum.")
	bravo()

def second_verse():
	girl_named_fred()
	print("My reasons must be clear.\nWhen she shows you all how strong she is you'll stand right up and cheer!")
	spell_fred()
	third_verse()

def third_verse():
	girl_named_fred()
	print("She drinks just like a lord!\nSo sing a merry drinking song and let the wine be poured!")
	fill_the_bowl()
	fourth_verse()

def fourth_verse():
	girl_named_fred()
	print("She sings just like a bird!\nYou'll be left completely speechless when her gentle voice is heard!")
	la_la()
	fifth_verse()

def fifth_verse():
	girl_named_fred()
	print("She wrestles like a Greek!\nYou will clap your hands in wonder at her fabulous technique!")
	clap()
	sixth_verse()

def sixth_verse():
	girl_named_fred()
	print("She dances with such grace!\nYou are bound to sing her praises 'til you're purple in the face!")
	bravo()
	seventh_verse()

def seventh_verse():
	girl_named_fred()
	print("She's musical to boot!\nShe will set your feet a-tapping when she plays upon her lute!")	
	strum()
	eight_verse()

def eight_verse():
	girl_named_fred()
	print("A clever, clownish wit!\nWhen she does her funny pantomime your sides are sure to split!\nHa ha ha ha, ho ho ho ho, ha ha ha ha ho!")	
	strum()
	ninth_verse()

def ninth_verse():
	print('''I'm in love with a girl.\nHe's in love with a girl named "F-R-E-D" Fred!''')

def main():
	print("I like you, Fred, I like you!" + 
		"\nYou're just saying those words to be kind.\nNo, I mean it.  I like... I mean I love you, Fred!\n" + 
		"He is out of his medieval mind!\nI'm perfectly sane and sound!  I never felt better in my life!\n" + 
		"Everybody... everybody, everybody!  Come on!  And meet my incipient wife!\n")
	second_verse()

main()