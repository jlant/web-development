import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

hidden_html = """
<input type="hidden" name="food" value="{}">
"""

item_html = """
<li>{}</li>
"""

shopping_list_html = """
<br>
<br>
<h2>Shopping List</h2>
<ul>
{}
</ul>
"""

class Handler(webapp2.RequestHandler):
    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

    def render_str(self, template, **kwargs):
        t = jinja_env.get_template(template)
        return t.render(kwargs)

    def render(self, template, **kwargs):
        self.write(self.render_str(template, **kwargs))

class MainPage(Handler):
    def get(self):
        n = self.request.get("n")
        if n:
            n = int(n)
        self.render("shopping_list.html", n = n)
        # output = form_html
        # output_hidden = ""

        # items = self.request.get_all("food")

        # if items:
        #     output_items = ""
        #     for item in items:
        #         output_hidden += hidden_html.format(item)
        #         output_items += item_html.format(item)

        #     output_shopping = shopping_list_html.format(output_items)
        #     output += output_shopping

        # output = output.format(output_hidden)

        # self.write(output)

class FizzBuzzHandler(Handler):
    def get(self):
        n = self.request.get("n", 0)
        n = n and int(n)
        self.render("fizzbuzz.html", n = n)
        

app = webapp2.WSGIApplication([("/", MainPage), 
                               ("/fizzbuzz", FizzBuzzHandler)], 
                               debug = True)