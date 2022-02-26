def setup():
    noStroke()


def draw():
    max_distance = dist(0, 0, width, height)
    background(255)

    for i in range(0, width + 1, 20):
        for y in range(0, height + 1, 20):
            size = dist(mouseX, mouseY, i, y)
            size = size / max_distance * 66
            ellipse(i, y, size, size)
