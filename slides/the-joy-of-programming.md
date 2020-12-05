
# The Joy of Programming
## Anand Chitipothu

---

# The circle

![right fit](../images/circle.png)

```
circle(300, 300, 100)
```

---

# Three Circles in a Row

![right fit](../images/three-circles-in-row.png)

```
circle(200, 300, 100)
circle(300, 300, 100)
circle(400, 300, 100)
```

---

# Three Concentric Circles

![right fit](../images/three-concentric-circles.png)

```
circle(300, 300, 100)
circle(300, 300, 200)
circle(300, 300, 300)
```

---


# Three Concentric Circles

![right fit](../images/three-concentric-circles-fn.png)

```
def concentric_circles(x, y, d, n):
    delta = d/n
    for i in range(1, n+1):
        circle(x, y, i*delta)

concentric_circles(300, 300, 300, 3)
```

---

# Ten Concentric Circles

![right fit](../images/concentric-circles-10.png)

```
concentric_circles(300, 300, 300, 10)
```

---

# Circles in a Grid

![right fit](../images/circles-in-grid.png)

```
def grid(shape, n):
    size = width/n
    for i in range(n):
        for j in range(n):
            cx = j*size + size/2
            cy = i*size + size/2
            shape(cx, cy, size)

grid(circle, 4)
```

---

# Circles in a Grid

![right fit](../images/grid-6-circles.png)

```
grid(circle, 6)
```

---

# Circles in a Grid

![right fit](../images/grid-16-circles.png)

```
grid(circle, 16)
```

---

# [fit] Concentric Circles in a Grid

![right fit](../images/grid-concentric-circles-3-4.png)

```
grid(
  lambda x, y, d:
    concentric_circles(x, y, d, 3),
  4)
```

---

# [fit] Concentric Circles in a Grid

![right fit](../images/grid-concentric-circles-3-4.png)

```
from functools import partial

grid(
  partial(concentric_circles, n=3),
  4)
```

---

# [fit] Concentric Circles in a Grid

![right fit](../images/grid-concentric-circles-5-4.png)

```
grid(
  partial(concentric_circles, n=5),
  4)
```
---

# [fit] Concentric Circles in a Grid

![right fit](../images/grid-concentric-circles-5-8.png)

```
grid(
  partial(concentric_circles, n=5),
  8)
```

---

# Randomness

---

# [fit] Random Concentric Circles

![right fit](../images/random-concentric-circles.png)

```
from random import random

def random_concentric_circles(
        x, y, d, n):
    for i in range(n):
        circle(x, y, random()*d)

random_concentric_circles(
    300, 300, 300, 10)
```
---

# [fit] Random Concentric Circles in a Grid

![right fit](../images/grid-random-circles-10-4.png)

```
grid(
  partial(
    random_concentric_circles,
    n=10),
  4)
```

---

# [fit] Random Concentric Circles in a Grid

![right fit](../images/grid-random-circles-10-16.png)

```
grid(
  partial(
    random_concentric_circles,
    n=16),
  4)
```
---

# Hypnotic Circles

---

# Hypnotic Circles

![right fit](../images/hypnotic-circles.png)

```
def hypnotic_circles(x, y, size, n=10):
    delta = size/n
    dx = random.choice([-0.5, 0, 0.5])
    dy = random.choice([-0.5, 0, 0.5])
    for i in range(n, 0, -1):
        d = delta*i
        circle(x, y, delta*i)
        x += dx*delta/2
        y += dy*delta/2


draw_grid(hypnotic_circles, 8)
```

---

# Something Fishy!

![inline fit](../images/fish.png)

---

# Fish!

![right fit](../images/fish.png)

```
fish = get_fish(border=True)
show(fish, scale=True, margin=100)
```
---

# Toolkit

**`flip(p)` :** _Flips p around the vertical axis._

**`rot(p)` :** _Rotates p by 90 degrees anti clockwise._

**`rot45(p)` :** _Rotates p by 45 degrees anti clockwise._

**`over(p, q)` :** _Draws shape p and q over each other._

**`above(p, q)` :** _Draws the shapes verticaly one above the other._

**`beside(p, q)` :** _Draws the shapes hortizontally one besides the other._

---

# Flip

Flips an image around the vertical axis.

![right fit](../images/fish-flip.png)

```
fish2 = flip(fish)
```

---

# `rot`

Flips an image anti-clockwise by 90 degrees.


![right fit](../images/fish-rot.png)

```
fish2 = rot(fish)
```

---

# `rot45`

Flips an image anti-clockwise by 45 degrees and scales down to fit the width of original image.

![right fit](../images/fish-rot45.png)

```
fish2 = rot45(fish)
```

---

# `over`

Places one image over the other.

![right fit](../images/fish-over.png)

```
fish2 = rot(rot(fish))
p = over(fish, fish2)
```

---

# `above`

Places one image over the other.

![right fit](../images/fish-above.png)

```
p = above(fish, fish)
```

---

# `beside`

Places one image over the other.

![right fit](../images/fish-beside.png)

```
p = beside(fish, fish)
```

---

# New Tools - quartlet

![right fit](../images/fish-quartlet.png)

```
def quartlet(p, q, r, s):
    return above(
        beside(p, q),
        beside(r, s))

z = quartlet(fish, fish, fish, fish)
```
---

# New Tools - nonet

![right fit](../images/fish-nonet.png)

```
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
```
---

## Cycle

![right fit](../images/fish-cycle.png)

```
def cycle(p):
    return quartlet(
        rot(p), p,
        rot(rot(p)), rot(rot(rot(p))))

z = cycle(fish)
```
---

# The tile `t`

The basic fish, three times.

![right fit](../images/fish-t.png)

```
fish2 = flip(rot45(fish))
fish3 = rot(rot(rot(fish2)))
t = over(fish, fish2, fish3)
```

---

# The tile `u`

The basic fish, four times.

![right fit](../images/fish-u.png)

```
u = over(
    fish2, rot(fish2),
    rot(rot(fish2)), rot(rot(rot(fish2)))
)
```

---

## Tesselate `u`

![right fit](../images/fish-u-quartlet.png)

```
x = quartlet(u, u, u, u)
```
---

## Tesselate `u`

![right fit](../images/fish-u-quartlet-2.png)

```
x = quartlet(u, u, u, u)
y = quartlet(x, x, x, x)
```

---

## Tesselate `u`

![right fit](../images/fish-u-quartlet-3.png)

```
x = quartlet(u, u, u, u)
y = quartlet(x, x, x, x)
z = quartlet(y, y, y, y)
```

---

## Square Limit - Center

![right fit](../images/fish-limit.png)

Lets start with the center.

```
squarelimit = nonet(
    blank, blank, blank,
    blank, u, blank,
    blank, blank, blank)
```

---

# Square Limit - Top Side

![right fit](../images/fish-side-1.png)

```
side1 = quartlet(blank, blank, rot(t), t)

squarelimit = nonet(
    blank, side1, blank,
    blank, u, blank,
    blank, blank, blank)
```

---

# Square Limit - Left Side

![right fit](../images/fish-side-1b.png)

```
side1 = quartlet(blank, blank, rot(t), t)

x = nonet(
    blank, side1, blank,
    rot(side1), u, blank,
    blank, blank, blank)
```
---

# [fit] Square Limit - Bottom Side

![right fit](../images/fish-side-1c.png)

```
side1 = quartlet(blank, blank, rot(t), t)

x = nonet(
    blank, side1, blank,
    rot(side1), u, blank,
    blank, rot(rot(side2)), blank)
```

---

# Square Limit - Right Side

![right fit](../images/fish-side-1d.png)

```
side1 = quartlet(blank, blank, rot(t), t)

x = nonet(
    blank, side1, blank,
    rot(side1), u, rot(rot(rot(side2))),
    blank, rot(rot(side2)), blank)
```

---

# Square Limit - Corners

![right fit](../images/fish-corners.png)

```
corner1 = quartlet(blank, blank, blank, u)

squarelimit = nonet(
  corner1, side1, rot(rot(rot(corner1))),
  rot(side1), u, rot(rot(rot(side1))),
  rot(corner1), rot(rot(side1)), rot(rot(corner1)))
```

---

# Square Limit - Level 2

![right fit](../images/fish-limit2.png)

```
side1 = quartlet(blank, blank, rot(t), t)
side2 = quartlet(side1, side1, rot(t), t)

corner1 = quartlet(blank, blank, blank, u)
corner2 = quartlet(corner1, side1, rot(side1), u)

squarelimit2 = nonet(
  corner2, side2, rot(rot(rot(corner2))),
  rot(side2), u, rot(rot(rot(side2))),
  rot(corner2), rot(rot(side2)), rot(rot(corner2)))
```

---

# Square Limit - Level 3

![right fit](../images/fish-limit3.png)

```
side1 = quartlet(blank, blank, rot(t), t)
side2 = quartlet(side1, side1, rot(t), t)
side3 = quartlet(side2, side2, rot(t), t)

corner1 = quartlet(blank, blank, blank, u)
corner2 = quartlet(corner1, side1, rot(side1), u)
corner3 = quartlet(corner2, side2, rot(side2), u)

squarelimit3 = nonet(
    corner3, side3, rot(rot(rot(corner3))),
    rot(side3), u, rot(rot(rot(side3))),
    rot(corner3), rot(rot(side3)), rot(rot(corner3)))
```