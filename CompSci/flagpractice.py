from drawingpanel import*
panel = DrawingPanel(800,585)

def america():
	canvas = panel.canvas
	panel.set_background("light blue")
	return canvas

def stars(x1,y1,x2,y2,space,space2):
	canvas = america()
	for j in range (1,10):
		if j % 2 != 0:
			for i in range(0,6):
				canvas.create_line(x1 + 20 + (space* i),y1+15 + (j*25),x2+25 + (space*i),y2+7+ (j*25), fill = "white")
				canvas.create_line(x1 +25 + (space* i),y1+7+ (j*25),x2+30 + (space* i),y2+15+ (j*25), fill = "white")
				canvas.create_line(x1 +30 + (space* i),y1+15+ (j*25),x2+35 + (space* i),y2+15+ (j*25), fill = "white")
				canvas.create_line(x1 +35 + (space* i),y1+15+ (j*25),x2+31 + (space* i),y2+20+ (j*25), fill = "white")
				canvas.create_line(x1 +31 + (space* i),y1+20+ (j*25),x2+33 + (space* i),y2+27+ (j*25), fill = "white")
				canvas.create_line(x1+33 + (space* i),y1+27+ (j*25),x2+25 + (space* i),y2+24+ (j*25), fill = "white")
				canvas.create_line(x1+25 + (space* i),y1+24+ (j*25),x2+17 + (space* i),y2+27+ (j*25), fill = "white")
				canvas.create_line(x1+17 + (space* i),y1+27+ (j*25),x2+19 + (space* i),y2+20+ (j*25), fill = "white")
				canvas.create_line(x1+19 + (space* i),y1+20+ (j*25),x2+15 + (space* i),y2+15+ (j*25), fill = "white")
				canvas.create_line(x1+15 + (space* i),y1+15+ (j*25),x2+20 + (space* i),y2+15+ (j*25), fill = "white")
		else:
			for i in range(1,6):
				canvas.create_line(x1+20 + (space2* i),y1+15 + (j*25),x2+25 + (space2*i),y2+7+ (j*25), fill = "white")
				canvas.create_line(x1+25 + (space2* i),y1+7+ (j*25),x2+30 + (space2*i),y2+15+ (j*25), fill = "white")
				canvas.create_line(x1+30 + (space2* i),y1+15+ (j*25),x2+35 +(space2* i),y2+15+ (j*25), fill = "white")
				canvas.create_line(x1+35 + (space2* i),y1+15+ (j*25),x2+31 + (space2* i),y2+20+ (j*25), fill = "white")
				canvas.create_line(x1+31 + (space2* i),y1+20+ (j*25),x2+33 + (space2* i),y2+27+ (j*25), fill = "white")
				canvas.create_line(x1+33 + (space2* i),y1+27+ (j*25),x2+25 + (space2* i),y2+24+ (j*25), fill = "white")
				canvas.create_line(x1+25 + (space2* i),y1+24+ (j*25),x2+17 + (space2* i),y2+27+ (j*25), fill = "white")
				canvas.create_line(x1+17 + (space2* i),y1+27+ (j*25),x2+19 + (space2* i),y2+20+ (j*25), fill = "white")
				canvas.create_line(x1+19 + (space2* i),y1+20+ (j*25),x2+15 + (space2* i),y2+15+ (j*25), fill = "white")
				canvas.create_line(x1+15 + (space2* i),y1+15+ (j*25),x2+20 + (space2* i),y2+15+ (j*25), fill = "white")

def stripes(x1,y1,x2,y2):
	canvas = america()
	for j in range(0,13):
		if j % 2 == 0:
			canvas.create_rectangle(x1,y1 + (45 * j),x2, y2 + (45 * j), fill = "red")
		else:
			canvas.create_rectangle(x1,y1 + (45 * j),x2, y2 + (45 * j), fill = "white")

		
def top_left(x1,y1,x2,y2):
	canvas = america()
	canvas.create_rectangle(x1,y1,x2,y2, fill = "dark blue")
	



def main():
	
	america()
	stripes(0,0,800,45)
	top_left(0,0,400,270)
	stars(5,-5,5,-5,63,49)
	panel.sleep()
	panel.clear()
	panel.update()



main()



