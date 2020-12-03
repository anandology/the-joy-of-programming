
fish = get_fish(border=True)
fish2 = flip(rot45(fish))
u = over(
    fish2, rot(fish2),
    rot(rot(fish2)), rot(rot(rot(fish2)))
)
x = quartlet(u, u, u, u)
show(x, scale=True, margin=100)
