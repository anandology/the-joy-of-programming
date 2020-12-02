from svg import SVG

class Sketch:
    def __init__(self, width=600, height=600):
        self.width = width
        self.height = height
        self.svg = SVG(width=width+1, height=height+1)
        self.background("white")

    def background(self, color):
        self.svg.rect(x=0, y=0,
            width=self.width,
            height=self.height,
            fill=color,
            stroke="none")

    def circle(self, x, y, d):
        self.svg.circle(cx=x, cy=y, r=d/2,
            stroke="black",
            fill="none")

    def line(self, x1, y1, x2, y2):
        self.svg.line(x1=x1, y1=y1, x2=x2, y2=y2, stroke="black")

    def rect(self, x, y, w, h):
        self.svg.rect(x=x, y=y, width=w, height=h,
            stroke="black",
            fill="none")

    def tostring(self):
        return self.svg.tostring()

    def render(self, code):
        g = self.get_globals()
        exec(code, g, g)
        return self.tostring()

    def get_globals(self):
        return {
            "circle": self.circle,
            "rect": self.rect,
            "line": self.line,
            "width": self.width,
            "height": self.height
        }

if __name__ == "__main__":
    s = Sketch()
    code = """
circle(200, 200, 100)
    """
    s.render(code)
    print(s.tostring())