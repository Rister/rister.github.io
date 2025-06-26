AUTHOR = 'Jeremy Rist'
SITENAME = 'My Portfolio'
SITESUBTITLE = 'A Showcase of Projects and Skills'
SITEURL = ''
SITEDESCRIPTION = 'Welcome to My Portfolio, a collection of my work, thoughts, and experiments.'
SITEIMAGE = 'theme/static/images/logo.png' # Path relative to SITEURL
FAVICON = 'theme/static/images/favicon.ico' # Path relative to SITEURL


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
MENUITEMS = [
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    # ('About', '/pages/about.html'), # Example for a page
]
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True # If you have static pages like 'About'

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives'] # Add other templates as needed
PAGINATED_TEMPLATES = {'index': None} # Updated to dict format; None uses DEFAULT_PAGINATION
