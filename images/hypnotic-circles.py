import random

def hypnotic_circles(x, y, size, n=10):
    delta = size/n
    dx = random.choice([-0.5, 0, 0.5])
    dy = random.choice([-0.5, 0, 0.5])
    for i in range(n, 0, -1):
        d = delta*i
        circle(x, y, delta*i)
        x += dx*delta/2
        y += dy*delta/2

draw_grid(hypnotic_circles, 8)
