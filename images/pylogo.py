
py = scale(2, 2, translate(-35, 20,  get_python(fill='#ffc331', stroke='#ffc331')))
py2 = scale(2, 2, translate(-35, 20,  get_python(fill='#366994', stroke='#366994')))
border = Node(
            'rect',
            x=0, y=0,
            width=260, height=260,
            stroke_dasharray="5,5",
            stroke="#888")

t = translate(30, -118, scale(0.9, 0.9, over(py, rot(rot(py2)))))
#t = over(border, t)

def quartlet(p, q, r, s):
    return above(
        beside(p, q),
        beside(r, s))

def tessalate(p, level):
    if level == 0:
        return p
    else:
        p = tessalate(p, level-1)
        return quartlet(p, p, p, p)

u = over(t, rot(t), rot(rot(t)), rot(rot(rot(t))))

v = rot45(u)
shape = tessalate(v, 3)
show(shape, scale=True)
