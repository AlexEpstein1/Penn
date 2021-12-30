def main():
	#first argument is file name
	#second argument is mode to open
	#'r' is read mean
	#'w' is write
	#'a' is appending
	#using 'lines' makes it appear as a list
	file_handler = open('random.txt', 'r')
	entire_file = file_handler.read()
	print(entire_file)
	#go back to beginning of the file, otherwise only prints once
	file_handler.seek(0)
	#all of the lines of text each line is an element of a list
	line = file_handler.readlines()
	print(line)
	line = file_handler.readlines()
	print(line)
	file_handler.close()
main()


def write_text(filename, string):
	lines = ['line1', 'line2']
	with open(filename, 'w+') as f:
		f.write('\n'.join(lines))
		f.writelines(['a','b', 'c'])
		f.seek(0)
		stuff = f.read()
		print(stuff)
write_text('random.txt')