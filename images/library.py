def draw_grid(shape, n):
    size = width/n

    for i in range(n):
        for j in range(n):
            x = j*size+size/2
            y = i*size+size/2
            shape(x, y, size)

def nonet(
        p, q, r,
        s, t, u,
        v, w, x):
    return above(
        beside(p, q, r),
        beside(s, t, u),
        beside(v, w, x))

fish = get_fish(border=True)
fish2 = flip(rot45(fish))
fish3 = rot(rot(rot(fish2)))
t = over(fish, fish2, fish3)
u = over(
    fish2, rot(fish2),
    rot(rot(fish2)), rot(rot(rot(fish2)))
)
side1 = quartlet(blank, blank, rot(t), t)
corner1 = quartlet(blank, blank, blank, u)
