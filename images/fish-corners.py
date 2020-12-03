corner1 = quartlet(blank, blank, blank, u)

x = nonet(
    corner1, side1, rot(rot(rot(corner1))),
    rot(side1), u, rot(rot(rot(side1))),
    rot(corner1), rot(rot(side1)), rot(rot(corner1)))

show(x, scale=True)