from drawingpanel import *
panel = DrawingPanel(500,500)
canvas = panel.canvas

def helper(n):
	draw_box(250,250,200)

def draw_box(x,y,d):
	canvas.create_polygon(x - d/2, y - d/2, x + d/2,y - d/2,x + d/2, y + d/2, x - d/2,y + d/2)

def draw_carpet(x,y,d,n):
	if n == 1:
		draw_box(x,y,d)

	draw_box(x,y,d)

	draw_gasket(x-d,y,d,n)
	draw_gasket(x,y,d,n)
	draw_gasket(x,y,d,n)
	draw_gasket(x,y,d,n)
	draw_gasket(x,y,d,n)
	draw_gasket(x,y,d,n)
	draw_gasket(x,y,d,n)
	draw_gasket(x,y,d,n)



def main():
	helper(1)
	

main()