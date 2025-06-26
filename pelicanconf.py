AUTHOR = 'Jeremy Rist'
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
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/jeremy-rist-83096822/'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/risterio-simple' # Direct relative path to the theme
# Removed THEME_PATHS
# Removed THEME_TEMPLATES_OVERRIDES
# TEMPLATE_PAGES = {'../templates/base.html': 'base.html'} # This line was incorrect and likely causing TypeErrors
MENUITEMS = [] # Define MENUITEMS, even if empty, for themes that expect it.
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives'] # Add other templates as needed
PAGINATED_TEMPLATES = {'index': None} # Updated to dict format; None uses DEFAULT_PAGINATION
