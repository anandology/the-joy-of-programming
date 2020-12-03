from random import random
from functools import partial

def random_concentric_circles(x, y, d, n):
    for i in range(n):
        circle(x, y, random()*d)

def grid(shape, n):
    size = width/n
    for i in range(n):
        for j in range(n):
            cx = j*size + size/2
            cy = i*size + size/2
            shape(cx, cy, size)

grid(
  partial(random_concentric_circles, n=10),
  4)
