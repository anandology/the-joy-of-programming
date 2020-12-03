
fish = get_fish(border=True)
fish2 = flip(rot45(fish))
fish3 = rot(rot(rot(fish2)))
t = over(fish, fish2, fish3)

show(t, scale=True, margin=100)
