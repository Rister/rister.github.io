# --- Basic Site Settings ---
AUTHOR = 'Jeremy Rist'
SITENAME = 'My Portfolio'
SITESUBTITLE = 'A Showcase of Projects and Skills'
SITEURL = '' # Define this in publishconf.py for production
SITEDESCRIPTION = 'Welcome to My Portfolio, a collection of my work, thoughts, and experiments.'
SITEIMAGE = 'static/images/placeholder.png' # Updated to existing placeholder. Was: static/images/logo.png
# FAVICON = 'static/images/favicon.ico' # Commented out as favicon.ico is missing. Was: static/images/favicon.ico

# --- Date & Time ---
import datetime
CURRENTYEAR = datetime.date.today().year
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# --- Content Paths & URLs ---
PATH = 'content' # Root for content files
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True # Good for development, set to False in publishconf.py

ARTICLE_PATHS = [''] # Look for articles in content/ root
PAGE_PATHS = ['pages'] # Look for pages in content/pages/

# Structure for generated URLs and file paths
ARTICLE_SAVE_AS = '{slug}.html'
ARTICLE_URL = '{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'

# --- Feeds ---
# Feed generation is usually not desired when developing, enable in publishconf.py if needed
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# === Navigation & Menu Settings ===
# Links to display in a "blogroll" section, often in the sidebar or footer
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Links to social media profiles, often displayed in the sidebar or footer
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/jeremy-rist-83096822/'),
          ('Another social link', '#'),) # Use # for placeholders

# Main menu items for the site navigation
MENUITEMS = [
    ('Archives', '/archives.html'), # Link to the archives page
    ('Categories', '/categories.html'), # Link to the categories page
    # ('About', '/pages/about.html'), # Example: Link to an "About" page
]
# These DISPLAY_*_ON_MENU settings are often theme-dependent.
# The theme's templates must be written to use these variables.
DISPLAY_CATEGORIES_ON_MENU = True # Automatically add categories to the menu
DISPLAY_PAGES_ON_MENU = True # Automatically add static pages to the menu

# === Pagination Settings ===
DEFAULT_PAGINATION = 10 # Number of articles per page if pagination is enabled
# Configure which templates should be paginated, e.g., {'index': None, 'archives': 10}
# `None` uses DEFAULT_PAGINATION.
# PAGINATED_TEMPLATES = {'index': None} # Example: Paginate the index page

# === Theme Settings ===
THEME = 'themes/ClutteredDesk' # Relative path to the theme directory
# Other theme-related settings (if any) would go here.
# E.g., THEME_STATIC_DIR = 'static', THEME_STATIC_PATHS = ['static'] (often defaults)
# The following were commented out as they were part of previous experiments or are not currently used:
# # Removed THEME_PATHS
# # Removed THEME_TEMPLATES_OVERRIDES
# # TEMPLATE_PAGES = {'../templates/base.html': 'base.html'}
# # INDEX_SAVE_AS = 'index.html'

# === Plugin Settings ===
PLUGIN_PATHS = ['pelican/plugins'] # List of paths where plugins are located
PLUGINS = ['humans'] # List of plugins to activate

# Settings specific to the 'humans' plugin (for humans.txt generation)
# These settings populate the content of the generated humans.txt file.
HUMANS_TEAM = [
    {'Author': 'Jeremy Rist', 'Role': 'Owner/Developer', 'Contact': 'jeremy@rist.dev'}
]
HUMANS_SITE = {
    'Standards': 'HTML5, CSS3',
    'Components': 'Pelican, Jinja2, IBM Plex Mono (from Google Fonts)', # Example components
    'Software': 'Python'
}
# Note: The /* SITE */ section in humans.txt will always include "Last update".

# === Template Generation Settings ===
# Defines which templates to render directly (e.g., index, archives, categories pages).
# These are typically top-level pages of your site.
DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
# Other direct templates could be 'tags', etc., depending on your site structure and theme.
# For custom static pages not managed as Pelican pages or articles (e.g., a custom landing page),
# you might use TEMPLATE_PAGES.
# Example: TEMPLATE_PAGES = {'src/custom_page.html': 'output/custom_page.html'}
# The PAGINATED_TEMPLATES setting (under Pagination) is related but specifically for paginated views.
# # PAGINATED_TEMPLATES = {'index': None} # Example from above, moved here for context if uncommented.

# --- Final check on existing commented out lines for context or removal ---
# # Removed THEME_PATHS -> This is fine, means we are not using THEME_PATHS setting.
# # Removed THEME_TEMPLATES_OVERRIDES -> Fine, not using template overrides this way.
# # TEMPLATE_PAGES = {'../templates/base.html': 'base.html'} # Incorrect usage, good that it's commented.
# # INDEX_SAVE_AS = 'index.html' # This is default behavior, explicitly setting it is usually not needed unless changing the name.
# # PAGINATED_TEMPLATES = {'index': None} # (already discussed under pagination)
# The HUMANS_TEAM and HUMANS_SITE settings that were here are duplicates of the ones
# already defined under the "=== Plugin Settings ===" section and have been removed.
# The comment "# The /* SITE */ section will always include "Last update"." is also noted with the primary settings.
