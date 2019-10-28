import random as rand
from math import *
from tkinter import *

class ppp:
    def __init__(self, root):
        self.Stroke_ = "black"
        self.Fill_="black"
        self.StrokeSize_ = 3
        self.sX = 500
        self.sY = 100
        self.mouseX = 0
        self.mouseY = 0
        self.canvas = Canvas(root, height=500, width=500, bg="white")
        self.canvas.grid(row=0, column=0)
        self.width = int(self.canvas.cget("width"))
        self.height = int(self.canvas.cget("height"))
        self.points = []
            
    def line(self, x, y, x2, y2):
        self.canvas.create_line(x, y, x2, y2, fill=self.Stroke_, width=self.StrokeSize_);
    
    def stroke(self, color):
        self.Stroke_ = color
    
    def fill(self, color):
        self.Fill_ = color
    
    def strokeSize(self, size):
        self.StrokeSize_ = size
    
    def ellipse(self, x, y, sizeX, sizeY):
        self.canvas.create_oval(x, y, x+sizeX, y+sizeY, width=self.StrokeSize_, fill=self.Fill_,
            outline=self.Stroke_)
    
    def rect(self, x, y, sizeX, sizeY):
        self.canvas.create_rectangle(x, y, x+sizeX, y+sizeY, width=self.StrokeSize_, fill=self.Fill_,
            outline=self.Stroke_)
    
    def background(self, bgfill):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.width+10, self.height+10, width=0, fill=bgfill)

    def polygon(self):
        self.canvas.create_polygon(self.points, width=self.StrokeSize_, fill=self.Fill_,
            outline=self.Stroke_)
        
    def text(self, t, x, y):
        self.canvas.create_text((x,y), text=t)

def line(x, y, x2, y2):
    _p.line(x, y, x2, y2)
    
def stroke(*args):
    color = ''
    if len(args) == 1:
        r = args[0]
        g = args[0]
        b = args[0]
        color = '#%02x%02x%02x' % (r, g, b)
    if len(args) == 3:
        r = args[0]
        g = args[1]
        b = args[2]
        color = '#%02x%02x%02x' % (r, g, b)
    if len(args) == 4:
        r = args[0]
        g = args[1]
        b = args[2]
        a = args[3]
        if not a:
            color = ''
    _p.stroke(color)

def noStroke():
    _p.Stroke_ = ""

def noFill():
    _p.fill("")

def background(*args):
    color = ''
    if len(args) == 1:
        r = args[0]
        g = args[0]
        b = args[0]
        color = '#%02x%02x%02x' % (r, g, b)
    if len(args) == 3:
        r = args[0]
        g = args[1]
        b = args[2]
        color = '#%02x%02x%02x' % (r, g, b)
    if len(args) == 4:
        r = args[0]
        g = args[1]
        b = args[2]
        a = args[3]
        if not a:
            color = ''
    _p.background(color)

def fill(*args):
    color = ''
    if len(args) == 1:
        r = args[0]
        g = args[0]
        b = args[0]
        color = '#%02x%02x%02x' % (r, g, b)
    if len(args) == 3:
        r = args[0]
        g = args[1]
        b = args[2]
        color = '#%02x%02x%02x' % (r, g, b)
    if len(args) == 4:
        r = args[0]
        g = args[1]
        b = args[2]
        a = args[3]
        if not a:
            color = ''
    _p.fill(color)

def strokeSize(thickness):
    _p.strokeSize(thickness)

def ellipse(x, y, sizeX, sizeY):
    _p.ellipse(x, y, sizeX, sizeY)
    
def rect(x, y, sizeX, sizeY):
    _p.rect(x, y, sizeX, sizeY)
   
def random(*args):
    if len(args) == 0:
        return rand.random()
    elif len(args) == 1:
        s = 0
        endnum = args[0]
        return rand.randint(s, endnum)
    elif len(args) == 2:
        s = args[0]
        e = args[1]
        return rand.randint(s, e)
    

def beginShape():
    _p.points = []

def vertex(x, y):
    _p.points.append(x)
    _p.points.append(y)

def endShape(*args):
    _p.polygon()

def dist(x1, y1, x2, y2):
    squared_delta_x = (x2 - x1) ** 2
    squared_delta_y = (y2 - y1) ** 2
    return sqrt(squared_delta_x + squared_delta_y)


    
from tkinter import *

root = Tk() 
root.title("processing python")

_p = ppp(root)
width = _p.width
height = _p.height

===||===

def motion(event):
    _p.mouseX, _p.mouseY = event.x, event.y
    #print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()
