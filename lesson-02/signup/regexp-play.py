import re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

def valid_username(username):

    return USER_RE.match(username)


def valid_verify(password, verify):

    return password == verify

def valid_email(email):

    return EMAIL_RE.match(email)

print(re.DEBUG)
print(valid_username("jeremiah")) #  good
print(valid_username("je"))  # None
print(valid_username("jere*"))  # None
print(valid_username("jeremiah1_-")) #  good
print(valid_username("")) #  None

print(valid_verify("hello", "hello"))  # True
print(valid_verify("hello", "hellothere"))  # False

print(valid_email("jlant@usgs.gov"))  # good
print(valid_email("jeremiah@gmail.com"))  # good
print(valid_email("j@gmail"))  # None
print(valid_email("jeremiah"))  # None