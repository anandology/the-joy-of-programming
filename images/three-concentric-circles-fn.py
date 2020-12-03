show_grid()

def concentric_circles(x, y, d, n):
    delta = d/n
    for i in range(1, n+1):
        circle(x, y, i*delta)

concentric_circles(300, 300, 300, 3)