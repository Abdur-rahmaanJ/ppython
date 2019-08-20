def setup():
    print(dist(0, 0, 0, 100))

def draw():
    #background(100)
    noStroke()
    fill(random(255))
    ellipse(10, 10, 100, random(50, 100))