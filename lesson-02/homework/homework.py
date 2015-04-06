import webapp2
import cgi

form = """
<form method="post">
    <h1>Enter some text to ROT13</h1>
    <br>
    <textarea rows="6" cols="50">Hello there!</textarea>
    <br>
    <input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(form)

application = webapp2.WSGIApplication([('/', MainPage),], debug=True)