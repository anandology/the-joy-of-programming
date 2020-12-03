"""Functional Geometry implementation in Python.

Credits:
Functional Geometry, Oct 2020 - Peter Henderson
https://eprints.soton.ac.uk/257577/1/funcgeo2.pdf

Sashi Gowda implemented the same concept in Julia.
The fish image is borrowed from his notebook.
http://shashi.biz/ijulia-notebooks/funcgeo/
"""
from svg import Node
import math

FISH = Node("path", d=open("fish.path").read().strip(), style="fill: black;")

def transform(shape, t):
    g = Node("g", transform=t)
    g.add_node(shape)
    return g

def rotate(angle, shape):
    t = f"translate(130, 130) rotate({angle}) translate(-130, -130)"
    return transform(shape, t)

def translate(x, y, shape):
    t = f"translate({x}, {y})"
    return transform(shape, t)

def rot(shape):
    return rotate(-90, shape)

def rot45(shape):
    s = 1/math.sqrt(2)
    return transform(shape, f"scale({s}, {s}) rotate(-45)")

def scale(xscale, yscale, shape):
    t = f"scale({xscale}, {yscale})"
    return transform(shape, t)

def flip(shape):
    return transform(shape, "translate(260, 0) scale(-1, 1)")

def over(*shapes):
    g = Node("g")
    for s in shapes:
        g.add_node(s)
    return g

def above(*shapes):
     h = 260/len(shapes)
     yscale = 1/len(shapes)
     shapes = [translate(0, h*i, scale(1, yscale, s)) for i, s in enumerate(shapes)]
     return over(*shapes)

def beside(*shapes):
     w = 260/len(shapes)
     xscale = 1/len(shapes)
     shapes = [translate(w*i, 0, scale(xscale, 1, s)) for i, s in enumerate(shapes)]
     return over(*shapes)

def quartlet(p, q, r, s):
    return above(
        beside(p, q),
        beside(r, s))

def make_path(size, points):
    points = [(x*size, y*size) for (x, y) in points]
    d = "M {} {} ".format(*points[0])
    for p in points[1:]:
        d += "L {} {} ".format(*p)
    return Node("path", d=d)

def get_fish(border=False, fill="black", stroke="black"):
    node = Node("path",
        d=open("fish.path").read().strip(),
        style=f"fill: {fill}; stroke={stroke};")
    if border:
        b = Node(
            'rect',
            x=0, y=0,
            width=260, height=260,
            stroke_dasharray="5,5",
            stroke="#888")
        return over(node, b)
    else:
        return node

def get_python(fill="black", stroke="black"):
    return Node("path",
        d=open("python.path").read().strip(),
        style=f"fill: {fill}; stroke: {stroke};")


F = make_path(260, [
    (.2, .1),
    (.8, .1),
    (.8, .2),
    (.3, .2),
    (.3, .5),
    (.6, .5),
    (.6, .6),
    (.3, .6),
    (.3, .9),
    (.2, .9),
    (.2, .1)
])

blank = Node("g")

exports = {
    "transform": transform,
    "translate": translate,
    "rotate": rotate,
    "scale": scale,

    "rot": rot,
    "rot45": rot45,
    "over": over,
    "above": above,
    "beside": beside,
    "quartlet": quartlet,

    "rot": rot,
    "flip": flip,
    "fish": FISH,
    "get_fish": get_fish,
    "get_python": get_python,
    "F": F,
    "blank": blank
}