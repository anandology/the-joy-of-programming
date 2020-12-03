import math

def display(shape):
    border = Node("rect",
        x=0, y=0,
        width=260, height=260,
        stroke_dasharray="5,5",
        stroke="#888")

    s = over(shape, border)

    show(scale(2.3, 2.3, shape))

blank = Node("g")

fish = Node("path", d=fish.attrs['d'], style= 'fill: #666; stroke: #666;')
fish2 = flip(rot45(fish))
fish3 = rot(rot(rot(fish2)))

t = over(fish, fish2, fish3)

u = over(fish2, rot(fish2), rot(rot(fish2)), rot(rot(rot(fish2))))

def nonet(
    p, q, r,
    s, t, u,
    v, w, x):
    return above(
       beside(p, q, r),
       beside(s, t, u),
       beside(v, w, x))

side1 = quartlet(blank, blank, rot(t), t)
side2 = quartlet(side1, side1, rot(t), t)
corner1 = quartlet(blank, blank, blank, u)
corner2 = quartlet(corner1, side1, rot(side1), u)

squarelimit2 = nonet(
    corner2, side2, rot(rot(rot(corner2))),
    rot(side2), u, rot(rot(rot(side2))),
    rot(corner2), rot(rot(side2)), rot(rot(corner2)))

display(squarelimit2)

fishx = Node("path", d=fish.attrs['d'], style= 'fill: red; stroke: red;')
fishx2 = flip(rot45(fishx))
ux = over(fishx2, blank, blank, blank)

s = nonet(
    blank, blank, blank,
    blank, ux, blank,
    blank, blank, blank)

display(s)
