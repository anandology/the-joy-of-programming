side1 = quartlet(blank, blank, rot(t), t)
side2 = quartlet(side1, side1, rot(t), t)

corner1 = quartlet(blank, blank, blank, u)
corner2 = quartlet(corner1, side1, rot(side1), u)

squarelimit2 = nonet(
    corner2, side2, rot(rot(rot(corner2))),
    rot(side2), u, rot(rot(rot(side2))),
    rot(corner2), rot(rot(side2)), rot(rot(corner2)))

show(squarelimit2, scale=True)