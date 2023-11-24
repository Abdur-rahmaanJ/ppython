image_path = "/Users/sahajathota/Downloads/FSE/Activity/Activity/ppython/ppython/snippets/Images/pastel.jpeg"
img = None
x, y = 200, 200  
x_speed, y_speed = 3, 2  
angle = 0

def setup():
    size(400, 400)
    global img
    img = loadImage(image_path)
    imageMode(CENTER)

def draw():
    global x, y, x_speed, y_speed, angle

    background(255)

    # Update position based on speed
    x += x_speed
    y += y_speed

    # Bounce off the walls
    if x > width - 75 or x < 75:
        x_speed *= -1
    if y > height - 75 or y < 75:
        y_speed *= -1

    translate(x, y)
    rotate(radians(angle))

    image(img, 0, 0, 150, 150)  

    angle += 5

