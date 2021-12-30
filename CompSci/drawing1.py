from drawingpanel import *

def box_drawing():
	panel = DrawingPanel(500,500)
	canvas = panel.canvas
	panel.set_background("purple")
	canvas.create_rectangle(0, 0, 500, 500, fill = "purple")
	for i in range(0,10):
		canvas.create_rectangle(0 +(i*25),0 +(i*25),500 - (i*25),500 - (i*25), fill = "purple")

	canvas.create_line(0, 500, 250, 250, fill = "forest green")
	canvas.create_line(250, 250, 500, 500, fill = "forest green")
def main():
	box_drawing()

main()