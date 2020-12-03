
def show_grid(width, height):
    size = 100
    for y in range(0, height+1, size):
        line(0, y, width, y, stroke="#aaa")

    for x in range(0, width+1, size):
        line(x, 0, x, height, stroke="#aaa")