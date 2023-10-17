import turtle
class Shape:
    def __init__(self, sides, size, color, line_thickness):
        self.sides=sides
        self.size=size
        self.color=color
        self.line_thickness=line_thickness
    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for e in range(self.sides):
            turtle.forward(self.size)
            turtle.right(128.5)
        turtle.done()
square=Shape(15,100,'yellow',10)
print(square.draw())
