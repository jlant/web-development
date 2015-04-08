import webapp2
import re

form = """
<h1>Signup</h1>
<form method="post">
    <table>
        <tr>
            <td class="label" style="text-align: right">
                Username
            </td>
            <td>
                <input type="text" name="username" value={username}>
            </td>
            <td class="error" style="color: red">
                {username_error}
            </td>
        </tr>
        <tr>
            <td class="label" style="text-align: right">
                Password
            </td>
            <td>
                <input type="password" name="password" value="">
            </td>
            <td class="error" style="color: red">
                {password_error}                
            </td>
        </tr>
        <tr>
            <td class="label" style="text-align: right">
                Verify Password
            </td>
            <td>
                <input type="password" name="verify" value="">
            </td>
            <td class="error" style="color: red">
                {verify_error}                
            </td>
        </tr>
        <tr>
            <td class="label" style="text-align: right">
                Email (optional)
            </td>
            <td>
                <input type="text" name="email" value={email}>
            </td>
            <td class="error" style="color: red">
                {email_error}                
            </td>
        </tr>
    </table>
    <input type="submit">
</form>
"""

welcome_page = """
<h1>Welcome {username}!</h1>
"""

# regular expressions for inputs
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

# error messages
USERNAME_ERROR = "That's not a valid username"
PASSWORD_ERROR = "That's wasn't a valid password"
VERIFY_ERROR = "Your passwords did not match"
EMAIL_ERROR = "That's not a valid email"

def valid_username(username):

    return USER_RE.match(username)

def valid_password(password):

    return PASSWORD_RE.match(password)

def valid_email(email):

    return EMAIL_RE.match(email)

def valid_verify(password, verify):

    return password == verify

class MainPage(webapp2.RequestHandler):
    
    def write_form(self, username = "", password = "", verify = "", email = "", 
                         username_error = "", password_error = "", verify_error = "", email_error = ""):

        self.response.out.write(form.format(username = username, 
                                            password = password, 
                                            verify = verify,
                                            email = email,
                                            username_error = username_error,
                                            password_error = password_error,
                                            verify_error = verify_error,
                                            email_error = email_error))

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.write_form()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        if not valid_username(username) and not valid_password(password):
            self.write_form(username = username, password = password, verify = verify, email = email,
                            username_error = USERNAME_ERROR, password_error = PASSWORD_ERROR)

        elif not valid_verify(password, verify):
            self.write_form(username = username, password = password, verify = verify, email = email,
                            verify_error = VERIFY_ERROR)

        elif email:
            if not valid_email(email):
                self.write_form(username = username, password = password, verify = verify, email = email,
                                email_error = EMAIL_ERROR)           
            else:
                self.redirect("/welcome?username=" + username)
        else:
            self.redirect("/welcome?username=" + username)

class WelcomeHandler(webapp2.RequestHandler):

    def write_form(self, username = ""):
        self.response.out.write(welcome_page.format(username = username))

    def get(self):
        username = self.request.get("username")
        self.write_form(username = username)

application = webapp2.WSGIApplication([("/", MainPage), ("/welcome", WelcomeHandler)], debug=True)