from drawingpanel import *
panel = DrawingPanel(500,500)
canvas = panel.canvas

def draw_htree(n):
	# n denotes recursion depth

	draw_htree_helper(250,250,200,n)

def drawH(x,y,d):
	canvas.create_line(x - (d/2),y - (d/2),x - (d/2),y + (d/2))
	canvas.create_line(x + (d/2),y - (d/2),x + (d/2),y + (d/2))
	canvas.create_line(x - (d/2),y ,x + (d/2) ,y)

def draw_htree_helper(x,y,d,n):
	#starting coordinates at center of H
	# helper recursive function
	if n ==1:
		#draw a single H
		drawH(x,y,d)
		return

	drawH(x,y,d)

	draw_htree_helper(x - d / 2,y - d / 2,d / 2,n-1)
	draw_htree_helper(x + d / 2,y - d / 2,d / 2,n-1)
	draw_htree_helper(x + d / 2,y + d / 2,d / 2,n-1)
	draw_htree_helper(x - d / 2,y + d / 2,d / 2,n-1)
	




def main():
	draw_htree(5)

main()