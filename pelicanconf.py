# Copyright (c) 2024 Jeremy Rist. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see https://opensource.org/licenses/MIT.

import datetime
from datetime import timezone

# --- Basic Site Settings ---
AUTHOR = "Jeremy Rist"
SITENAME = "My Portfolio"
SITESUBTITLE = "A Showcase of Projects and Skills"
SITEURL = ""  # Define this in publishconf.py for production
SITEDESCRIPTION = (
    "Welcome to My Portfolio, a collection of my work, thoughts, and experiments."
)
SITEIMAGE = "static/images/placeholder.png"  # Updated to existing placeholder. Was: static/images/logo.png

# --- Date & Time ---
CURRENTYEAR = datetime.datetime.now(timezone.utc).year
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"

# --- Content Paths & URLs ---
PATH = "content"  # Root for content files
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True  # Good for development, set to False in publishconf.py

ARTICLE_PATHS = [""]  # Look for articles in content/ root
PAGE_PATHS = ["pages"]  # Look for pages in content/pages/
STATIC_PATHS = ["static", "images"]  # Directories to copy to output, relative to PATH (content/)


# Structure for generated URLs and file paths
ARTICLE_SAVE_AS = "{slug}.html"
ARTICLE_URL = "{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"
PAGE_URL = "pages/{slug}.html"
CATEGORY_SAVE_AS = "category/{slug}.html"
CATEGORY_URL = "category/{slug}.html"
TAG_SAVE_AS = "tag/{slug}.html"
TAG_URL = "tag/{slug}.html"

# --- Feeds ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# === Navigation & Menu Settings ===
# Links to display in a "blogroll" section, often in the sidebar or footer
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Links to social media profiles, often displayed in the sidebar or footer
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/jeremy-rist-83096822/"),
    ("Another social link", "#"),
)  # Use # for placeholders

# Main menu items for the site navigation
MENUITEMS = [
    ("Archives", "/archives.html"),  # Link to the archives page
    ("Categories", "/categories.html"),  # Link to the categories page
]
# These DISPLAY_*_ON_MENU settings are often theme-dependent.
# The theme's templates must be written to use these variables.
DISPLAY_CATEGORIES_ON_MENU = True  # Automatically add categories to the menu
DISPLAY_PAGES_ON_MENU = True  # Automatically add static pages to the menu

# === Pagination Settings ===
DEFAULT_PAGINATION = 10  # Number of articles per page if pagination is enabled

# === Theme Settings ===
THEME = "themes/ClutteredDesk"  # Relative path to the theme directory

# === Plugin Settings ===
PLUGIN_PATHS = ["pelican/plugins"]  # List of paths where plugins are located
PLUGINS = ["humans"]  # List of plugins to activate

# Settings specific to the 'humans' plugin (for humans.txt generation)
# These settings populate the content of the generated humans.txt file.
HUMANS_TEAM = [
    {"Author": "Jeremy Rist", "Role": "Owner/Developer", "Contact": "jeremy@rist.dev"},
]
HUMANS_SITE = {
    "Standards": "HTML5, CSS3",
    "Components": "Pelican, Jinja2, IBM Plex Mono (from Google Fonts)",  # Example components
    "Software": "Python",
}
# Note: The /* SITE */ section in humans.txt will always include "Last update".

# Defines which templates to render directly (e.g., index, archives, categories pages).
# These are typically top-level pages of your site.
DIRECT_TEMPLATES = ["index", "categories", "authors", "archives"]


