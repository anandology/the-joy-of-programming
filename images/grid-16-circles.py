
def grid(shape, n):
    size = width/n
    for i in range(n):
        for j in range(n):
            cx = j*size + size/2
            cy = i*size + size/2
            shape(cx, cy, size)

grid(circle, 16)
