import cgi

def escape_html(s):
    return cgi.escape(s, quote = True)

def escape_html2(s):
    for (i, o) in (("&", "&amp;"),
                   (">", "&gt;"),
                   ("<", "&ls;"),
                   ('"', "&quot;")):
      s = s.replace(i, o)
    return s

print(escape_html("<b>html!</b>"))