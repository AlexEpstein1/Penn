from drawingpanel import*

panel = DrawingPanel(640,480)
panel.set_background("orange")
canvas = panel.canvas

class Ball(object):
	def __init__(self, radius, locationx, locationy, color = "cyan"):
		self.radius = radius
		self.locationx = locationx
		self.locationy = locationy
		self.color = color
		self.vx = 10
		self.vy = 10

	def draw(self):
		canvas.create_oval(self.locationx - self.radius, self.locationy - self.radius, self.locationx + self.radius, self.locationy + self.radius, fill = "blue")

	def update(self):
		self.locationx += self.vx
		self.locationy += self.vy

		if self.locationx <= 0:
			self.vx = -self.vx

		if self.locationx >= 640:
			self.vx = -self.vx

		if self.locationy <= 0:
			self.vy = -self.vy 

		if self.locationy >= 480:
			self.vy = -self.vy


ball = Ball(4, 0 , -1, "red")
while 1:
	ball.draw()
	panel.sleep(30)
	canvas.delete("all")
	ball.update()


