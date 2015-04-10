import webapp2
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template, **kwargs):
    t = jinja_env.get_template(template)
    return t.render(**kwargs)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kwargs):
        self.response.out.write(render_str(template, **kwargs))

    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

class Rot13(BaseHandler):
    def get(self):
        self.render("rot13-form.html")

    def post(self):
        rot13 = ""
        text = self.request.get("text")
        if text:
            rot13 = text.encode("rot13")

        self.render("rot13-form.html", text = rot13)

app = webapp2.WSGIApplication([("/", Rot13),], debug = True)