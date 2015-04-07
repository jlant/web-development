import webapp2
import cgi

form = """
<form method="post">
    <h1>Enter some text to ROT13</h1>
    <br>
    <textarea name="text" rows="6" cols="50">{text}</textarea>
    <br>
    <p>{error}</p>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    
    def write_form(self, error = "", text = "Hello there!"):
        self.response.out.write(form.format(error = error, text = text))

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    def post(self):
        text = self.request.get("text")
        rot13_text = text.encode("rot13")
        self.write_form(text = rot13_text)

application = webapp2.WSGIApplication([('/', MainPage),], debug=True)