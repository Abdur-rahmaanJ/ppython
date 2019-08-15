#from ppp import *
from random import *
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
            
    def line(self, x, y, x2, y2):
        self.canvas.create_line(x, y, x2, y2, fill=self.Stroke_, width=self.StrokeSize_);
    
    def stroke(self, r, g, b):
        self.Stroke_ = '#%02x%02x%02x' % (r, g, b)
    
    def fill(self, r, g, b):
        self.Fill_ = '#%02x%02x%02x' % (r, g, b)
    
    def strokeSize(self, size):
        self.StrokeSize_ = size
    
    def ellipse(self, x, y, sizeX, sizeY):
        self.canvas.create_oval(x, y, x+sizeX, y+sizeY, width=self.StrokeSize_, fill=self.Fill_)
    
    def rect(self, x, y, sizeX, sizeY):
        self.canvas.create_rectangle(x, y, x+sizeX, y+sizeY, width=self.StrokeSize_, fill=self.Fill_)
    
    def background(self, r, g, b):
        self.canvas.delete("all")
        bgfill = '#%02x%02x%02x' % (r, g, b)
        self.canvas.create_rectangle(0, 0, self.width+10, self.height+10, width=0, fill=bgfill)

def line(x, y, x2, y2):
    _p.line(x, y, x2, y2)
    
def stroke(r, g, b):
    _p.stroke(r, g, b)

def noStroke():
    _p.strokeSize(0)

def noFill():
    _p.fill("")

def background(r, g, b):
    _p.background(r, g, b)

def fill(r, g, b):
    _p.fill(r, g, b)

def strokeSize(thickness):
    _p.strokeSize(thickness)

def ellipse(x, y, sizeX, sizeY):
    _p.ellipse(x, y, sizeX, sizeY)
    
def rect(x, y, sizeX, sizeY):
    _p.rect(x, y, sizeX, sizeY)
   
def random(s, e):
    #global random
    return randint(s, e)


    
from tkinter import *

root = Tk() 
root.title("processing python")

_p = ppp(root)
width = _p.width
height = _p.height

class Particle:
    def __init__(self, x, y, r=10, vx=1, vy=1, randv=False):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy

        if randv:
            rand1 = random(0, 1)
            rand2 = random(0, 1)
            if rand1:
                self.vx *= -1
            if rand2:
                self.vy *= -1


    def draw(self):
        noStroke()
        fill(140,70,20)
        ellipse(self.x, self.y, self.r, self.r)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def check_bounds(self):
        global width
        if self.x > width-self.r or self.x-self.r < 0:
            self.vx *= -1
        if self.y > height-self.r or self.y-self.r < 0:
            self.vy *= -1

    def run(self):
        self.update()
        self.check_bounds()
        self.draw()

particles = [Particle(
                random(0, width), random(0, width), vx=2, vy=2, randv=True) 
            for i in range(200)]
def setup():
    global width, height, mouseX, mouseY
    pass

def draw():
    global root, width, height, mouseX, mouseY
    mouseX = _p.mouseX; mouseY = _p.mouseY
    global particles
    background(255, 255, 255)
    for p in particles:
        p.run()
    root.after(30, draw)
setup()
draw()

#self.canvas.create_rectangle(20, 50, 200, 100, outline="black", fill="red", width=2, stipple="gray50")
#fill("orange")
#ircle(10, 10)
# ################

def motion(event):
    _p.mouseX, _p.mouseY = event.x, event.y
    #print('{}, {}'.format(x, y))

root.bind('<Motion>', motion)
root.mainloop()