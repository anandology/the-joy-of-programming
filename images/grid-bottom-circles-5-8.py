from functools import partial

def grid(shape, n):
    size = width/n
    for i in range(n):
        for j in range(n):
            cx = j*size + size/2
            cy = i*size + size/2
            shape(cx, cy, size)

def circle_with_bottom(x, y, d):
    cx = x
    cy = y-d/2
    circle(cx, cy, d)

def growing(x, y, d, shape, n, xoffset=0, yoffset=0):
    delta = d/n
    x += xoffset * d
    y += yoffset * d
    for i in range(1, n+1):
        shape(x, y, i*delta)

bottom_touching_circles = partial(
    growing,
    shape=circle_with_bottom,
    yoffset=0.5,
    n=5)

grid(bottom_touching_circles, 8)