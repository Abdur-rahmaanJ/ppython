import math

def draw_branch(length, angle, start_x, start_y):
    angle = angle % 360
    if 0 < angle < 90:
        end_x = start_x + (length * math.sin(math.radians(90-angle)))
        end_y = start_y - (length * math.sin(math.radians(angle)))
    elif angle == 90:
        end_x = start_x
        end_y = start_y - length
    elif 180 > angle > 90:
        end_x = start_x - (length * math.cos(math.radians(180-angle)))
        end_y = start_y - (length * math.sin(math.radians(180-angle)))
    elif angle == 180:
        end_x = start_x - length
        end_y = start_y
    elif 270 > angle > 180:
        end_x = start_x - (length * math.cos(math.radians(angle - 180)))
        end_y = start_y + (length * math.sin(math.radians(angle - 180)))
    elif angle == 270:
        end_x = start_x
        end_y = start_y + length
    elif 360 > angle > 270:
        end_x = start_x + (length * math.cos(math.radians(360 - angle)))
        end_y = start_y + (length * math.sin(math.radians(360 - angle)))
    elif angle == 0 or angle == 360:
        end_x = start_x + length
        end_y = start_y
    line(start_x, start_y, end_x, end_y)
    return end_x, end_y

def draw_branches(start_x, start_y, previous_branch_len, previous_angle):
    global angle_factor
    if previous_branch_len <= 10:
        return
    length_factor = 2/3
    current_branch_len = previous_branch_len * length_factor
    current_left_branch_angle = previous_angle + angle_factor
    next_x, next_y = draw_branch(current_branch_len, current_left_branch_angle, start_x, start_y)
    draw_branches(next_x, next_y, current_branch_len, current_left_branch_angle)

    current_right_branch_angle = previous_angle - angle_factor
    next_x, next_y = draw_branch(current_branch_len, current_right_branch_angle, start_x, start_y)
    draw_branches(next_x, next_y, current_branch_len, current_right_branch_angle)

def setup():
    stroke(255, 0, 255)
    strokeSize(1)

def draw():
    global angle_factor
    background(0, 0, 0)
    init_branch_len = 150
    init_angle = 90
    start_x, start_y = draw_branch(init_branch_len, init_angle, width/2, height)
    angle_factor = (mouseX/width) * init_angle
    draw_branches(start_x, start_y, init_branch_len, init_angle)