"""Functional Geometry implementation in Python.

Credits:
Functional Geometry, Oct 2020 - Peter Henderson
https://eprints.soton.ac.uk/257577/1/funcgeo2.pdf

Sashi Gowda implemented the same concept in Julia.
The fish image is borrowed from his notebook.
http://shashi.biz/ijulia-notebooks/funcgeo/
"""
from svg import Node

FISH = Node("path", d=open("fish.path").read().strip())

def rotate(angle, shape):
    g = Node("g", transform=f"translate(130, 130) rotate({angle}) translate(-130, -130)")
    g.add_node(shape)
    return g

def rot(shape):
    return rotate(-90, shape)

def over(a, b):
    g = Node("g")
    g.add_node(a)
    g.add_node(b)
    return g