
import jinja2
import os

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

print(template_dir)
print(os.path.abspath(template_dir))

def render_str(template, **kwargs):
    t = jinja_env.get_template(template)
    print t

render_str("rot13-form.html")