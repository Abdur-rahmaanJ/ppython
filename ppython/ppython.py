import os
import sys

def handle(text):
    tab = "    "
    nl = "\n"
    glob_set = "global width, height, mouseX, mouseY"
    glob_draw = "global root, width, height, mouseX, mouseY\n    mouseX = _p.mouseX; mouseY = _p.mouseY"
    others = ()
    setup = "def setup():"
    draw = "def draw():"
    
    text= ""+text.replace(setup,setup+nl+tab+glob_set)
    text= ""+text.replace(draw,draw+nl+tab+glob_draw)
    text = "" + text + '\n    ' + "root.after(30, draw)"
    if (text.find(setup) != -1):
        text = ""+text+"\nsetup()"
    if (text.find(draw) != -1):
        text = ""+text+"\ndraw()"    
    with open("template.py","r") as f:
        z=f.read()
        z=z.replace("===||===",text)
        #print(z)
     
    fw = open("dump/dump.py","w+")
    fw.write(z)
    fw.flush()
    fw.close()
    import dump.dump # hack way of running file
    
    #with open("myF.py") as f:
    #    exec(f.read())

# print(sys.argv)
with open(sys.argv[1]) as f:
    handle(f.read())