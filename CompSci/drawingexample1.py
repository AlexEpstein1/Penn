from drawingpanel import *

def simple_drawing():
	
	panel = DrawingPanel(640,480)
	canvas = panel.canvas

	canvas.create_oval(100,100,250,250, fill = "lightgreen")

def main():
	simple_drawing()

main()