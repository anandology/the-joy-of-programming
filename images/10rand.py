import random

def draw_grid(shape, n):
    size = width/n

    for i in range(n):
        for j in range(n):
            x = j*size+size/2
            y = i*size+size/2
            shape(x, y, size)

def slantLine(x, y, size):
    if random.random() < 0.5:
        line(
          x-size/2, y-size/2,
          x+size/2, y+size/2)
    else:
        line(
          x-size/2, y+size/2,
          x+size/2, y-size/2)

draw_grid(slantLine, 4)
