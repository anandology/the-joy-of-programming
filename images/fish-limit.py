def nonet(
        p, q, r,
        s, t, u,
        v, w, x):
    return above(
        beside(p, q, r),
        beside(s, t, u),
        beside(v, w, x))

x = nonet(
    blank, blank, blank,
    blank, u, blank,
    blank, blank, blank)

show(x, scale=True)
