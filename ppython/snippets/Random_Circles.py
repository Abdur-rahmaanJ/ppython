def setup():
    size(400, 400)
    background(255)
    noStroke()

def draw():
    for i in range(10):
        x = random(width)
        y = random(height)
        diameter = random(20, 50)
        pastel_color = color(random(150, 255), random(150, 255), random(150, 255))
        fill(pastel_color)
        ellipse(x, y, diameter, diameter)
