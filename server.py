import web
import json
import os
from sketch import Sketch

urls = (
    "/", "redirect /default",
    "/([^/]*)", "index",
    "/([^/]*)/render", "render",
)
app = web.application(urls, globals())

def jsonify(d):
    web.header("Content-type", "application/json")
    return json.dumps(d)

def read_file(name):
    filename = f"files/{name}.py"
    if os.path.exists(filename):
        return open(filename).read()
    else:
        return ""

def write_file(name, code):
    filename = f"files/{name}.py"
    print("writing", filename)
    with open(filename, "w") as f:
        f.write(code)

class index:
    def GET(self, name):
        web.header("content-type", "text/html")
        code = web.websafe(read_file(name))
        html = open("index.html").read()
        return html.replace("<!--CODE-->", code)

class render:
    def POST(self, name):
        code = web.data().decode('utf-8')
        write_file(name, code)
        try:
            s = Sketch()
            s.render(code)
            return s.tostring()
        except Exception as e:
            web.ctx.status = "403 Bad Input"
            web.header("content-type", "text/plain")
            return str(e)

if __name__ == "__main__":
    app.run()