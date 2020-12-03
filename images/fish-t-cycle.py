
def cycle(p):
    return quartlet(
        rot(p), p,
        rot(rot(p)), rot(rot(rot(p))))

x = cycle(t)
show(x, scale=True, margin=100)
