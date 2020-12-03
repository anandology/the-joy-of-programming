
def cycle(p):
    return quartlet(
        rot(p), p,
        rot(rot(p)), rot(rot(rot(p))))

z = cycle(fish)
show(z, scale=True, margin=100)
