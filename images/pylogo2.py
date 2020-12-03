
py = scale(2, 2, translate(-35, 20,  get_python(fill='#ffc331', stroke='#ffc331')))
py2 = scale(2, 2, translate(-35, 20,  get_python(fill='#366994', stroke='#366994'))) 
border = Node(
            'rect',
            x=0, y=0,
            width=260, height=260,
            stroke_dasharray="5,5",
            stroke="#888")

t = translate(-110, 20, scale(0.85, 0.85, over(py, rot(rot(py2)))))
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

u = quartlet(rot(t), t, rot(rot(t)), rot(rot(rot(t))))

#v = rot45(t)
#shape = tessalate(u, 1)
v = translate(-65, -65, over(u, translate(130, 130, u)))
shape = tessalate(v, 2)
show(shape, scale=True, margin=50)
