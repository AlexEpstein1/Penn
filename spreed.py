from drawingpanel import*
import sys 

def animate_text(filename, width, height, font_size, wpm):
	panel = DrawingPanel(width, height)

	canvas = panel.canvas
	with open(filename, 'r') as f:
		words_list = f.read().split()
		for i in range(len(words_list)):
			canvas.create_text(width/2 - 18 * .5, height/2, anchor = 'e', font = ('Courier', font_size), text = helper(words_list[i])[0])
			canvas.create_text(width/2, height/2, font = ('Courier', font_size), text = helper(words_list[i])[1], fill = 'orange')
			canvas.create_text(width/2 + 18 * .5, height/2, anchor= 'w', font = ('Courier', font_size), text = helper(words_list[i])[2])
			

			if (words_list[i])[-1] in [".",",",";"]:
				panel.sleep(120000/wpm)	
			
			else:
				panel.sleep(60000/wpm)
			panel.clear()

def helper(words_list):
	if len(words_list) == 1:
		return ["", words_list[0], ""]

	elif len(words_list) >=2 and len(words_list) <=5: 
		return [words_list[0], words_list[1], words_list[2:]]

	elif len(words_list) >=6 and len(words_list)  <=9:
		return [words_list[0:2], words_list[2], words_list[3:]]

	elif len(words_list) >= 10 and len(words_list) <= 13:
		return [words_list[0:3], words_list[3], words_list[4:]]

	elif len(words_list) > 13:
		return [words_list[0:4], words_list[4], words_list[5:]]

def main():
	animate_text(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])) 

main()