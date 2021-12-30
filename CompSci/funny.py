from drawingpanel import *
panel = DrawingPanel(500,500)
canvas = panel.canvas

def balls(x1,y1,x2,y2,size):
	for i in range(2):
		canvas.create_oval(x1 + (i*size), y1, x2 + (i*size), y2)

def shaft(x1,y1,x2,y2,size):
	canvas.create_oval(x1 + size/2, y1, x2 - size/2, y2)

def main():
	balls(200,200,250,250,50)
	shaft(200,240,300,400,50)

main()

