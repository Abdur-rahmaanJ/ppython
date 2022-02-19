def setup():
    background(0)
    strokeSize(20)

    for w in range(width):
        stroke(random(0, 255), random(0, 255), random(0, 255))
        line(w, 0, w, height)


def draw():
    pass
