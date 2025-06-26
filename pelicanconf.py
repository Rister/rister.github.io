AUTHOR = 'Test User'
SITENAME = 'My Portfolio'
SITEURL = ''

import datetime
CURRENTYEAR = datetime.date.today().year

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/risterio-simple'
# TEMPLATE_PAGES = {'../templates/base.html': 'base.html'} # This line was incorrect and likely causing TypeErrors
MENUITEMS = [] # Define MENUITEMS, even if empty, for themes that expect it.
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives'] # Add other templates as needed
PAGINATED_TEMPLATES = {'index': None} # Updated to dict format; None uses DEFAULT_PAGINATION
