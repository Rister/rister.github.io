AUTHOR = 'Jeremy Rist'
SITENAME = 'My Portfolio'
SITESUBTITLE = 'A Showcase of Projects and Skills'
SITEURL = ''
SITEDESCRIPTION = 'Welcome to My Portfolio, a collection of my work, thoughts, and experiments.'
SITEIMAGE = 'static/images/logo.png' # Path relative to SITEURL
FAVICON = 'static/images/favicon.ico' # Path relative to SITEURL


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
RELATIVE_URLS = True

# Article and page paths - recommended by theme AGENTS.md
ARTICLE_PATHS = [''] # Look for articles in content/ root
PAGE_PATHS = ['pages'] # Assuming pages are in 'content/pages/'
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
# Category and Tag paths, if needed by theme or for organization
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'

PLUGIN_PATHS = ['pelican/plugins']
PLUGINS = ['humans']


THEME = 'themes/BinderPaper' # Direct relative path to the theme
# Removed THEME_PATHS
# Removed THEME_TEMPLATES_OVERRIDES
# TEMPLATE_PAGES = {'../templates/base.html': 'base.html'} # This line was incorrect and likely causing TypeErrors
# INDEX_SAVE_AS = 'index.html' # Removing this to see if it helps


MENUITEMS = [
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    # ('About', '/pages/about.html'), # Example for a page
]
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True # If you have static pages like 'About'

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives'] # Add other templates as needed
# PAGINATED_TEMPLATES = {'index': None} # Updated to dict format; None uses DEFAULT_PAGINATION - Removing for test


# Humans.txt Plugin Settings
HUMANS_TEAM = [
    {'Author': 'Jeremy Rist', 'Role': 'Owner/Developer', 'Contact': 'jeremy@rist.dev'}
]
HUMANS_SITE = {
    'Standards': 'HTML5, CSS3',
    'Components': 'Pelican, Jinja2, IBM Plex Mono (from Google Fonts)',
    'Software': 'Python'
}
# The /* SITE */ section will always include "Last update".
