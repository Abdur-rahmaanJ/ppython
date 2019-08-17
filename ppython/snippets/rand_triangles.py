def triangle(x1, y1, x2, y2, x3, y3):
    beginShape()
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    endShape()

def setup():
    background(255)
    noStroke()
    for x in range(0, width, 50):
        for y in range(0, width, 50):
            fill(random(0, 255), random(0, 255), random(0, 255))
            triangle(
                random(x, x+50),
                random(y, y+50),
                random(x, x+50),
                random(y, y+50),
                random(x, x+50),
                random(y, y+50)
                )

def draw():
    pass