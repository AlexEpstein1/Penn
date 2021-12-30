def write_text(filename, string):
	initials = input("Enter your initials. ")
	score = ranch_collected
	with open(filename, 'w+') as high_score:
		value = (initials + score)
		s = str(value)
		high_score.write(s)
		high_score.writelines([s])
write_text('highscore.txt')