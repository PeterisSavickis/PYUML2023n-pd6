import turtle
import math

class Canvas:
    def __init__(self, w, h):
        self.__visibleObjects = []   #list of shapes to draw
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = w, height = h)
        self.__turtle.hideturtle()

    def drawAll(self):
        self.__turtle.reset()
        self.__turtle.up()
        self.__screen.tracer(0)
        for shape in self.__visibleObjects: #draw all shapes in order
            shape._draw(self.__turtle)
        self.__screen.tracer(1)
        self.__turtle.hideturtle()

    def addShape(self, shape):
        self.__visibleObjects.append(shape)

    def draw(self, gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.__turtle.up()
        self.__screen.tracer(0)
        gObject._draw(self.__turtle)
        self.__screen.tracer(1)
        self.addShape(gObject)

from abc import *
class GeometricObject(ABC):
    def __init__(self):
        self.__lineColor = 'black'
        self.__lineWidth = 1
        self.__visible = False
        self.__myCanvas = None

    def setColor(self, color):  #modified to redraw visible shapes
        self.__lineColor = color
        if self.__visible:
            self.__myCanvas.drawAll()

    def setWidth(self, width):  #modified to redraw visible shapes
        self.__lineWidth = width
        if self.__visible:
            self.__myCanvas.drawAll()

    def getColor(self):
        return self.__lineColor

    def getWidth(self):
        return self.__lineWidth

    @abstractmethod
    def _draw(self):
        pass

    def setVisible(self, vFlag):
        self.__visible = vFlag

    def getVisible(self):
        return self.__visible

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas

    def getCanvas(self):
        return self.__myCanvas

class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        self.__coordinates = (x, y)

    def getCoord(self):
        return self.__coordinates

    def getX(self):
        return self.__coordinates[0]

    def getY(self):
        return self.__coordinates[1]

    def set_coordinates(self, x, y):
        self.__coordinates = (x, y)

    def _draw(self, turtle):
        turtle.goto(self.__coordinates[0], self.__coordinates[1])
        turtle.dot(self.getWidth(), self.getColor())

class Line(GeometricObject):
    def __init__(self, p1, p2):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__p1.getCoord())
        turtle.down()
        turtle.goto(self.__p2.getCoord())

class Triangle(GeometricObject):
    def __init__(self, point1, point2, point3):
        super().__init__()
        self.__points = [point1, point2, point3]

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__points[0].getCoord())
        turtle.down()
        for point in self.__points[1:]:
            turtle.goto(point.getCoord())
        turtle.goto(self.__points[0].getCoord())  # Closing the shape

class Rectangle(GeometricObject):
    def __init__(self, point1, point2):
        super().__init__()
        # Calculate the other two corners
        point3 = Point(point1.getX(), point2.getY())
        point4 = Point(point2.getX(), point1.getY())
        self.__points = [point1, point3, point2, point4]

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__points[0].getCoord())
        turtle.down()
        for point in self.__points[1:]:
            turtle.goto(point.getCoord())
        turtle.goto(self.__points[0].getCoord())  # Closing the shape

class Octagon(GeometricObject):
    def __init__(self, points):
        super().__init__()
        if len(points) != 8:
            raise ValueError("Octagon requires 8 points")
        self.__points = points

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__points[0].getCoord())
        turtle.down()
        for point in self.__points[1:]:
            turtle.goto(point.getCoord())
        turtle.goto(self.__points[0].getCoord())  # Closing the shape

def test2():
    myCanvas = Canvas(500, 500)
    line1 = Line(Point(-100, -100), Point(100, 100))
    line2 = Line(Point(-100, 100), Point(100, -100))
    line1.setWidth(4)    
    myCanvas.draw(line1)
    myCanvas.draw(line2)
    line1.setColor('red')
    line2.setWidth(4)
    turtle.done()

def drawTriangle():
    myCanvas = Canvas(500, 500)
    triangle = Triangle(Point(0, 100), Point(-100, -100), Point(100, -100))
    triangle.setWidth(2)
    triangle.setColor('blue')
    myCanvas.draw(triangle)
    turtle.done()

def drawRectangle():
    myCanvas = Canvas(500, 500)
    rectangle = Rectangle(Point(-100, 100), Point(100, -100))
    rectangle.setWidth(3)
    rectangle.setColor('green')
    myCanvas.draw(rectangle)
    turtle.done()

def create_regular_octagon(center, side_length):
    points = []
    for i in range(8):
        angle_deg = 45 * i
        angle_rad = math.radians(angle_deg)
        x = center.getX() + side_length * math.cos(angle_rad)
        y = center.getY() + side_length * math.sin(angle_rad)
        points.append(Point(x, y))
    return Octagon(points)

def drawOctagon():
    myCanvas = Canvas(500, 500)
    # Assuming create_regular_octagon is a method to create a regular octagon
    octagon = create_regular_octagon(Point(0, 0), 50)
    octagon.setWidth(4)
    octagon.setColor('red')
    myCanvas.draw(octagon)
    turtle.done()


drawOctagon()