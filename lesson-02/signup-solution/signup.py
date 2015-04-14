import webapp2
import jinja2
import os
import re

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

# regular expressions for inputs
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

# error messages
USERNAME_ERROR = "That's not a valid username"
PASSWORD_ERROR = "That's not a valid password"
VERIFY_ERROR = "Your passwords did not match"
EMAIL_ERROR = "That's not a valid email"

def valid_username(username):

    return username and USER_RE.match(username)

def valid_password(password):

    return password and PASSWORD_RE.match(password)

def valid_email(email):

    return not email or EMAIL_RE.match(email)

def render_str(template, **kwargs):
    t = jinja_env.get_template(template)
    return t.render(**kwargs)

class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kwargs):
        self.response.out.write(render_str(template, **kwargs))

    def write(self, *args, **kwargs):
        self.response.out.write(*args, **kwargs)

class Signup(BaseHandler):
    
    def get(self):
        self.render("signup-form.html")

    def post(self):
        have_error = False
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")   
        
        params = dict(username = username, email = email)    

        if not valid_username(username):
            params["username_error"] = USERNAME_ERROR
            have_error = True

        if not valid_password(password):
            params["password_error"] = PASSWORD_ERROR
            have_error = True
        elif password != verify:
            params["verify_error"] = VERIFY_ERROR
            have_error = True

        if not valid_email(email):
            params["email_error"] = EMAIL_ERROR
            have_error = True

        if have_error:
            self.render("signup-form.html", **params)
        else:
            self.redirect("/welcome?username=" + username)

class WelcomeHandler(BaseHandler):

    def get(self):
        username = self.request.get("username")
        if valid_username(username):
            self.render("welcome.html", username = username)
        else:
            self.redirect("/")

application = webapp2.WSGIApplication([("/", Signup), ("/welcome", WelcomeHandler)], debug=True)