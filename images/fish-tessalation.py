
fish = get_fish(border=True)
fish2 = flip(rot45(fish))

def cycle(shape):
    return over(
        shape,
        rot(shape),
        rot(rot(shape)),
        rot(rot(rot(shape))))

def quartlet(p, q, r, s):
    return above(
        beside(p, q), 
        beside(r, s))

u = over(fish2, rot(fish2), rot(rot(fish2)), rot(rot(rot(fish2))))


def tessalate(p, level):
    if level == 0:
        return p
    else:
        p = tessalate(p, level-1)
        return quartlet(p, p, p, p)

v = quartlet(u, u, u, u)
v2 = quartlet(v, v, v, v) 

t = over(fish, fish2, rot(rot(rot(fish2))))

shape = quartlet(rot(t), t, rot(rot(t)), rot(rot(rot(t))))

show(tessalate(shape, 4),  scale=True)
