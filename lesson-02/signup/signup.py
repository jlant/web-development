import webapp2

form = """
<h1>Signup</h1>
<form method="post">
    <table>
        <tr>
            <td class="label" style="text-align: right">
                Username
            </td>
            <td>
                <input type="text" name="username" value="">
            </td>
            <td class="error" style="color: red">
                Error!
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
                
            </td>
        </tr>
        <tr>
            <td class="label" style="text-align: right">
                Email (optional)
            </td>
            <td>
                <input type="text" name="email" value="">
            </td>
            <td class="error" style="color: red">
                
            </td>
        </tr>
    </table>
    <input type="submit">
    <p>{username}</p>
    <p>{password}</p>
    <p>{verify}</p>
    <p>{email}</p>
</form>
"""

welcome_page = """
<h1>Welcome {username}!</h1>
"""
class MainPage(webapp2.RequestHandler):
    
    def write_form(self, username = "", password = "", verify = "", email = ""):
        self.response.out.write(form.format(username = username, 
                                            password = password, 
                                            verify = verify,
                                            email = email))

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.write_form()

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        # self.write_form(username = username, password = password, verify = verify, email = email)

        self.redirect("/welcome?username=" + username)

class WelcomeHandler(webapp2.RequestHandler):

    def write_form(self, username = ""):
        self.response.out.write(welcome_page.format(username = username))

    def get(self):
        username = self.request.get("username")
        self.write_form(username = username)

application = webapp2.WSGIApplication([("/", MainPage), ("/welcome", WelcomeHandler)], debug=True)