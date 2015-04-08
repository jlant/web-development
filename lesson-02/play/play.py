import webapp2
import cgi

form = """
<form method="post">
    What is your birthday?
    <br>
    <label> 
        Month
        <input type="text" name="month" value={month}>
    </label>
    <label> 
        Day
        <input type="text" name="day" value={day}>
    </label>
    <label> 
        Year
        <input type="text" name="year" value={year}>
    </label>
    <div style="color: red">{error}</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

months = ["January",
          "Februrary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

month_abbvs = dict((m[:3].lower(),m) for m in months)

def valid_month(month):
    month = month.lower().capitalize()
    short_month = month[:3].lower()
    return month_abbvs.get(short_month)

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year <= 2020:
            return year

def escape_html(s):
    return cgi.escape(s, quote = True)

class MainPage(webapp2.RequestHandler):
    
    def write_form(self, error="", month="", day="", year=""):

      self.response.out.write(form.format(error = error, 
                                          month = escape_html(month), 
                                          day = escape_html(day), 
                                          year = escape_html(year)
                                          )
      )

    # get handler - draws the form
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.write_form()

    # post handler - posts to the url which happens when we submit the form
    def post(self):

        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")

        # check if user input is valid
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year):
            self.write_form(error = "That does not look right to me, friend.",
                            month = user_month, 
                            day = user_day,
                            year = user_year
            )
        else:
            self.redirect("/thanks")  # redirect to an different url

class ThanksHandler(webapp2.RequestHandler):

  def get(self):
    self.response.out.write("Thanks! That's a valid day.")

application = webapp2.WSGIApplication([('/', MainPage), ("/thanks", ThanksHandler)], debug=True)

