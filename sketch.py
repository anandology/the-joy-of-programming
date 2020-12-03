from svg import SVG, Node
import geometry as g
import os.path

class Sketch:
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.svg = SVG(viewBox=f"0 0 {width} {height}", style="stroke: black; fill: none;")
        self.background("white")

    def background(self, color):
        self.svg.rect(x=0, y=0,
            width=self.width,
            height=self.height,
            fill=color,
            stroke="none")

    def circle(self, x, y, d):
        self.svg.circle(cx=x, cy=y, r=d/2)

    def line(self, x1, y1, x2, y2, **kwargs):
        self.svg.line(x1=x1, y1=y1, x2=x2, y2=y2, **kwargs)

    def rect(self, x, y, w, h):
        self.svg.rect(x=x, y=y, width=w, height=h)

    def path(self, d):
        self.svg.path(d=d, stroke="black")

    def show(self, node, margin=0, scale=False, size=260):
        if margin or scale:
            s = (self.width-2*margin)/size if scale else 1
            g = Node("g", transform=f"translate({margin}, {margin}) scale({s}, {s})")
            g.add_node(node)
            self.svg.add_node(g)
        else:
            self.svg.add_node(node)

    def tostring(self):
        return self.svg.tostring()

    def render(self, code):
        g = self.get_globals()
        exec(code, g, g)
        return self.tostring()


    def show_grid(self):
        size = 100
        for y in range(0, self.height+1, size):
            self.line(0, y, self.width, y, stroke="#ccc")

        for x in range(0, self.width+1, size):
            self.line(x, 0, x, self.height, stroke="#ccc")

    def get_globals(self):
        return {
            "circle": self.circle,
            "rect": self.rect,
            "line": self.line,
            "path": self.path,
            "width": self.width,
            "height": self.height,
            "show_grid": self.show_grid,

            "Node": Node,
            "show": self.show,

            **g.exports
        }

def main():
    import sys
    filenames = sys.argv[1:]
    code = "\n".join(open(f).read() for f in filenames)
    s = Sketch()
    s.render(code)
    print(s.tostring())

if __name__ == "__main__":
    main()
