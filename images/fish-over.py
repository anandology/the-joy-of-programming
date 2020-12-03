
fish = get_fish(border=True)
fish2 = rot(rot(fish))
p = over(fish, fish2)

shape = quartlet(fish, fish2, p, blank)
show(p, scale=True, margin=100)