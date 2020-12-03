from random import random

def random_concentric_circles(x, y, d, n):
    for i in range(n):
        circle(x, y, random()*d)

random_concentric_circles(300, 300, 300, 10)