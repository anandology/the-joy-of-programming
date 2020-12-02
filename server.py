import web
import json
from sketch import Sketch

urls = (
    "/", "index",
    "/render", "render"
)
app = web.application(urls, globals())

def jsonify(d):
    web.header("Content-type", "application/json")
    return json.dumps(d)

class index:
    def GET(self):
        web.header("content-type", "text/html")
        return open("index.html").read()

class render:
    def POST(self):
        code = web.data()
        s = Sketch()
        s.render(code)
        return s.tostring()

if __name__ == "__main__":
    app.run()