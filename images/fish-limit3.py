side1 = quartlet(blank, blank, rot(t), t)
side2 = quartlet(side1, side1, rot(t), t)
side3 = quartlet(side2, side2, rot(t), t)

corner1 = quartlet(blank, blank, blank, u)
corner2 = quartlet(corner1, side1, rot(side1), u)
corner3 = quartlet(corner2, side2, rot(side2), u)

squarelimit3 = nonet(
    corner3, side3, rot(rot(rot(corner3))),
    rot(side3), u, rot(rot(rot(side3))),
    rot(corner3), rot(rot(side3)), rot(rot(corner3)))

show(squarelimit3, scale=True)