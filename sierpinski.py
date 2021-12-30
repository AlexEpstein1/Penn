from math import *
from drawingpanel import*
panel = DrawingPanel(500,500)
canvas = panel.canvas
panel.set_background("white")

def first_triangle(x1,y1):
	l = 500
	x2 = x1+l/2
	y2 = y1 - (l/2 * sqrt(3))
	x3 = x1 + l
	y3 = y1
	canvas.create_polygon(x1,y1,x2,y2,x3,y3, fill = "green")

def triangle(x1, y1, d, n):
	x2 = x1 + d
	y2 = y1
	x3 = x1+ (d/2)
	y3 = y1 + (sqrt(3) * d/2)
	if n != 0:
		canvas.create_polygon(x1,y1,x2,y2,x3,y3, fill = "black")
			

def sierpinski(x,y,d,n):
	if n > 1:
		triangle((x+250)/2, (y+66.975)/2, d/2,n) 
		triangle((x+0)/2, (y+500)/2, d/2,n)
		triangle((x+500)/2, (y+500)/2, d/2,n)
 	
	if n >= 2:
 		sierpinski((x+250)/2,(y+66.975)/2,d/2, n-1)
 		sierpinski((x+0)/2,(y+500)/2,d/2, n-1)
 		sierpinski((x+500)/2, (y+500)/2, d/2, n-1)
 		panel.sleep(5)

def main():
	n = int(input("Enter an n value: "))
	first_triangle(0,500)
	triangle(125, 283.4875, 500/2,n)
	sierpinski(125, 283.4875, 500/2, n)

main()
