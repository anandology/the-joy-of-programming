
side1 = quartlet(blank, blank, rot(t), t)

x = nonet(
    blank, side1, blank,
    rot(side1), u, rot(rot(rot(side1))),
    blank, rot(rot(side1)), blank)

show(x, scale=True)
