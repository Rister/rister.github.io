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
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican/plugins']
PLUGINS = ['humans'] # When using PLUGIN_PATHS, short names are often used

THEME = 'themes/BinderPaper' # Direct relative path to the theme
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

# Humans.txt Plugin Settings
# Example configuration:
# HUMANS_TEAM = [
#     {'Team member': 'Name', 'Role': 'Developer', 'Contact': 'email@example.com'},
#     'Another Team Member - Designer',
# ]
# HUMANS_THANKS = [
#     'Contributor Name - Contribution',
#     ('Another Contributor', 'Their Contribution'),
# ]
# HUMANS_SITE = {
#     'Standards': 'HTML5, CSS3, WCAG AAA',
#     'Components': 'Pelican, Jinja2, MyCustomTheme',
#     'Software': 'Python, VSCode',
# }
#
# By default, if these are not set, the plugin will use generic information.
# You can override specific sections or leave them for defaults.
# For example, to only specify the team:
HUMANS_TEAM = [
    {'Author': 'Jeremy Rist', 'Role': 'Owner/Developer', 'Contact': 'jeremy@rist.dev'}
]
HUMANS_SITE = {
    'Standards': 'HTML5, CSS3',
    'Components': 'Pelican, Jinja2, IBM Plex Mono (from Google Fonts)',
    'Software': 'Python'
}
# The /* SITE */ section will always include "Last update".
