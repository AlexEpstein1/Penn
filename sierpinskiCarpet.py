from drawingpanel import *
panel = DrawingPanel(500,500, "green")
canvas = panel.canvas

def draw_carpet(n):
	helper(250,250,200,n)

def draw_box(x,y,d):
	canvas.create_polygon(x - d/2, y - d/2, x + d/2,y - d/2,x + d/2, y + d/2, x - d/2,y + d/2, fill = "black")

def helper(x,y,d,n):
	if n == 1:
		draw_box(x,y,d)
		return

	draw_box(x,y,d)

	helper(x-d,y-d,d/3,n-1)
	helper(x-d,y,d/3,n-1)
	helper(x-d,y+d,d/3,n-1)
	helper(x+d,y+d,d/3,n-1)
	helper(x+d,y-d,d/3,n-1)
	helper(x+d,y,d/3,n-1)
	helper(x,y+d,d/3,n-1)
	helper(x,y-d,d/3,n-1)
	panel.sleep(5)



def main():
	draw_carpet(5)
	

main()