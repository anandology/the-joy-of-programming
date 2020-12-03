
fish = get_fish(border=True)
fish2 = flip(fish)

shape = quartlet(fish, fish2, blank, blank)
show(shape, scale=True, margin=100)