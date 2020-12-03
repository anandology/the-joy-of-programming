def nonet(
        p, q, r,
        s, t, u,
        v, w, x):
    return above(
        beside(p, q, r),
        beside(s, t, u),
        beside(v, w, x))

z = nonet(
    fish, fish, fish,
    fish, fish, fish,
    fish, fish, fish)

show(z, scale=True, margin=100)
