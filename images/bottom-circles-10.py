show_grid()

def circle_with_bottom(x, y, d):
    cx = x
    cy = y-d/2
    circle(cx, cy, d)

def bottom_touching_circles(x, y, d, n):
    delta = d/n
    for i in range(1, n+1):
        circle_with_bottom(x, y, i*delta)

bottom_touching_circles(300, 400, 300, 10)