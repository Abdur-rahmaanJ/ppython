def setup():
    background(80)
    noStroke()
    fill(255)
    # first
    beginShape()
    vertex(250, 20)
    vertex(200, 120)
    vertex(300, 120)
    endShape()

    beginShape()
    vertex(250, 220)
    vertex(200, 120)
    vertex(300, 120)
    endShape()

    # left
    beginShape()
    vertex(250, 220)
    vertex(140, 220)
    vertex(200, 320)
    endShape()

    beginShape()
    vertex(90, 320)
    vertex(140, 220)
    vertex(200, 320)
    endShape()

    # right
    beginShape()
    vertex(250, 220)
    vertex(360, 220)
    vertex(300, 320)
    endShape()

    beginShape()
    vertex(410, 320)
    vertex(360, 220)
    vertex(300, 320)
    endShape()


def draw():
    pass
