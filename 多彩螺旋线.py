Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> def draw_spin():
	colores = ['blue','yellow','red','purple','green','orange']
	turtle.bgcolor('black')
	for x in range(300):
		turtle.pencolor (colores[x % 6])
		turtle.width(x/100 + 1)
		turtle.forward (x)
		turtle.right(59)

		
>>> draw_spin()