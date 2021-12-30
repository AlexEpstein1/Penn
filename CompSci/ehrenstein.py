from drawingpanel import *
panel = DrawingPanel(500,500)

def ehrenstein():
	canvas = panel.canvas
	panel.set_background("green")
	return canvas

def square(x1,y1,x2,y2):
	canvas = ehrenstein()
	canvas.create_rectangle(x1, y1, x2, y2, fill = "cyan")

def circles(x1,x2,y1,y2, amount, size):
	canvas = ehrenstein()
	for  i in range (0,amount):
		canvas.create_oval(x1 + (i * size ), y1 + (i * size), x2 - (i *size), y2 - (i * size), fill = "yellow")

def lines(x1,x2,y1,y2,radius):
	canvas = ehrenstein()
	canvas.create_line(x1, y1 + radius, x2  - radius, y2, fill = "black")
	canvas.create_line(x1, y1 + radius, x2  - radius, y2 - (radius*2), fill = "black")
	canvas.create_line(x1 + radius, y1 + (radius*2), x2, y2 - radius, fill = "black")
	canvas.create_line(x1 +radius, y1, x2, y2-radius, fill = "black")

def circle_all(x1, y1, x2, y2, amount,size,radius):
	square(x1,y1,x2,y2)
	circles(x1,x2,y1,y2, amount,size)
	lines(x1,x2,y1,y2,radius)

def circle2(x1, y1, x2, y2, amount,size):
	circles(x1,x2,y1,y2, amount,size)

def middle(x1, y1, x2, y2, amount,size,radius):
	for j in range(3):
		for i in range(3):
			circle_all(x1+(i*(radius*2)), y1+(j*(radius*2)), x2+(i*(radius*2)), y2+(j*(radius*2)), amount,size,radius)

def top_left(x1, y1, x2, y2, amount,size,radius):
	circle_all(x1,x2,y1,y2, amount,size,radius)
	
def top(x1, y1, x2, y2, amount,size,radius):
	for i in range(7):
			circle_all(x1+(i*radius*2), y1, x2+(i*radius*2), y2, amount,size,radius)

def bottom(x1, y1, x2, y2, amount,size, radius):
	for j in range(2):
		for i in range(10):
			circle2(x1+(i*(radius*2)), y1+(j*(radius*2)), x2+(i*(radius*2)), y2+(j*(radius*2)), amount,size)

def left(x1, y1, x2, y2, amount,size, radius):
	for j in range(5):
		for i in range(2):
			circle_all(x1+(i*(radius*2)), y1+(j*(radius*2)), x2+(i*(radius*2)), y2+(j*(radius*2)), amount,size,radius)

def main():
	ehrenstein()
	middle(175,115,275,215,8,6,50)
	top_left(0,75,0,75,6,5,(75/2))
	top(105, 15, 155, 65, 10, 3, 25)
	bottom(200, 430, 225, 455, 4, 3, (25/2))
	left(10, 100, 80, 170, 3, 10, 35)

main()