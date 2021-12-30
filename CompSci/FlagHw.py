from drawingpanel import*
panel = DrawingPanel(800, 585)

def america():
	canvas = panel.canvas
	panel.set_background("light blue")
	return canvas

def stars_complete(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,x11,y11,space,space2):
	canvas = america()

	for j in range (1,10):
		if j % 2 != 0:
			for i in range(0,6):
				canvas.create_polygon(x1+ (space* i),y1+ (j*25),x2+ (space* i),y2+ (j*25),x3+ (space* i),y3+ (j*25),x4+ (space* i),y4+ (j*25),x5+ (space* i),y5+ (j*25),x6+ (space* i),y6+ (j*25),x7+ (space* i),y7+ (j*25),x8+ (space* i),y8+ (j*25),x9+ (space* i),y9+ (j*25),x10+ (space* i),y10+ (j*25),x11+ (space* i),y11+ (j*25), fill = "white")

		else:
			for i in range(1,6):
				canvas.create_polygon(x1+ (space2* i),y1+ (j*25),x2+ (space2* i),y2+ (j*25),x3+ (space2* i),y3+ (j*25),x4+ (space2* i),y4+ (j*25),x5+ (space2* i),y5+ (j*25),x6+ (space2* i),y6+ (j*25),x7+ (space2* i),y7+ (j*25),x8+ (space2* i),y8+ (j*25),x9+ (space2* i),y9+ (j*25),x10+ (space2* i),y10+ (j*25),x11+ (space2* i),y11+ (j*25), fill = "white")

def stripes_right(x1,y1,x2,y2):
	canvas = america()
	for j in range(0,6):
		if j % 2 == 0:
			canvas.create_rectangle(x1,y1 + (45 * j),x2, y2 + (45 * j), fill = "red")
		else:
			canvas.create_rectangle(x1,y1 + (45 * j),x2, y2 + (45 * j), fill = "white")

def stripes_bottom(x1,y1,x2,y2):
	canvas = america()
	for j in range(0,7):
		if j % 2 == 0:
			canvas.create_rectangle(x1,y1 + (45 * j),x2, y2 + (45 * j), fill = "red")
		else:
			canvas.create_rectangle(x1,y1 + (45 * j),x2, y2 + (45 * j), fill = "white")


		
def top_left(x1,y1,x2,y2):
	canvas = america()
	canvas.create_rectangle(x1,y1,x2,y2, fill = "dark blue")
	
def main():
	america()
	stripes_right(300,0,800,45)
	stripes_bottom(0,270,800,315)
	top_left(0,0,300,270)
	stars_complete(20,15,25,7,30,15,35,15,31,20,33,27,25,24,17,27,19,20,15,15,20,15,47,35.5)

main()