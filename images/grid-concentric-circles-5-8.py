from functools import partial

def grid(shape, n):
    size = width/n
    for i in range(n):
        for j in range(n):
            cx = j*size + size/2
            cy = i*size + size/2
            shape(cx, cy, size)

def concentric_circles(x, y, d, n):
    delta = d/n
    for i in range(1, n+1):
        circle(x, y, i*delta)

grid(partial(concentric_circles, n=5), 8)