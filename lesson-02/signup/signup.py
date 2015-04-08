import webapp2

form = """
<h1>Signup</h1>
<form>
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
</form>
"""

class MainPage(webapp2.RequestHandler):
    
    def write_form(self):
        self.response.out.write(form)

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.write_form()

    def post(self):
        pass

application = webapp2.WSGIApplication([("/", MainPage),], debug=True)