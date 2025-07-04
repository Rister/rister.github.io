## Agent Instructions for BinderPaper Theme

This document provides guidance for AI agents working on the Pelican `BinderPaper` theme.

### Theme Overview

The `BinderPaper` theme aims to replicate the look and feel of lined binder or notebook paper. Key features include:
- Off-white paper background.
- Light blue horizontal ruled lines.
- A vertical pink/red margin line on the left.
- A monospaced or "handwritten" primary font (currently 'Special Elite').

### File Structure

- **`static/css/BinderPaper.css`**: Main stylesheet for the theme. All visual styling related to the binder paper effect, typography, and layout should be here.
- **`templates/`**: Contains the Jinja2 templates for Pelican.
    - `base.html`: The main site skeleton. Links the CSS and defines common header/footer. The core `.content-wrapper` div that receives the paper styling is here.
    - `article.html`: Template for individual articles.
    - `index.html`: Template for the article list/homepage.
    - `page.html`: Template for static pages.
    - `pagination.html`: Template for pagination controls.
- **`AGENTS.md`**: This file.

### Development and Testing

1.  **Pelican Installation**: Ensure you have Pelican installed (`pip install pelican markdown`).
2.  **Sample Site**: To test changes, it's recommended to have a minimal Pelican site:
    *   Create a directory for your test site (e.g., `test_binder_site`).
    *   Inside it, create `pelicanconf.py`:
        ```python
        AUTHOR = 'Test User'
        SITENAME = 'BinderPaper Test Site'
        SITEURL = '' # Set to your local server for testing if needed

        PATH = 'content'
        TIMEZONE = 'UTC'
        DEFAULT_LANG = 'en'

        # Theme settings
        THEME = 'themes/BinderPaper' # Assuming pelicanconf.py is in the project root
        # Or, if your test site is in a directory like `test_site`
        # and `themes` is a sibling to `test_site`, then:
        # THEME = '../themes/BinderPaper' # Adjust path as needed

        # Feed generation is usually not required for theme testing
        FEED_ALL_ATOM = None
        CATEGORY_FEED_ATOM = None
        TRANSLATION_FEED_ATOM = None
        AUTHOR_FEED_ATOM = None
        AUTHOR_FEED_RSS = None

        # Blogroll
        LINKS = (('Pelican', 'https://getpelican.com/'),
                 ('Python.org', 'https://www.python.org/'),)

        # Social widget
        SOCIAL = (('You can add links in your config file', '#'),
                  ('Another social link', '#'),)

        DEFAULT_PAGINATION = 10

        # Uncomment following line if you want document-relative URLs when developing
        # RELATIVE_URLS = True

        # Article and page paths
        ARTICLE_PATHS = ['articles']
        PAGE_PATHS = ['pages']
        ARTICLE_SAVE_AS = '{slug}.html'
        ARTICLE_URL = '{slug}.html'
        PAGE_SAVE_AS = 'pages/{slug}.html'
        PAGE_URL = 'pages/{slug}.html'
        ```
    *   Create a `content/` directory in your test site.
    *   Inside `content/`, create `articles/` and add a sample Markdown file (e.g., `sample-post.md`):
        ```markdown
        Title: My First Post
        Date: 2023-01-01 10:00
        Category: Test
        Tags: pelican, test
        Author: Test User
        Summary: This is a test post for the BinderPaper theme.

        This is the main content of the post. It should appear on the "binder paper".

        ## A Subheading

        Some more text, with a [link to Pelican](https://getpelican.com/).

        ```python
        # This is a code block
        print("Hello, Binder!")
        ```

        > This is a blockquote. It should be styled appropriately.
        ```
    *   Generate the site: From your Pelican project root (containing `pelicanconf.py`), run `pelican content`. If `THEME` is set correctly in `pelicanconf.py`, it will use it.
    *   Alternatively, to explicitly specify the theme path during generation (e.g., if `pelicanconf.py` is elsewhere or you want to override): `pelican content -s pelicanconf.py -o output -t themes/BinderPaper` (run from project root).
    *   Preview: Open `output/index.html` or `output/my-first-post.html` in a browser. Or use `pelican --listen -r` from the project root.

3.  **CSS Line Height**: The `line-height` property in `BinderPaper.css` for text elements (like `p`, `li`) is critical for aligning text with the background ruled lines. If you change font sizes or line spacing, ensure the `background-image` gradient in `.content-wrapper` is adjusted accordingly, or vice-versa. The current line height is `24px`.

4.  **Font**: The theme uses 'Special Elite' from Google Fonts. If this font is changed, ensure the new font fits the skeuomorphic design.

### Coding Conventions

- Follow standard HTML5 and CSS3 practices.
- Ensure Jinja2 templating syntax is correct.
- Keep CSS selectors specific enough to avoid conflicts but general enough for reusability.
- Comment complex CSS or template logic.

### Future Enhancements Considerations (Optional)

-   **Hole punches**: Could be added to the left margin.
-   **Dog-eared corner**: A visual cue for a page corner.
-   **More paper textures/variations**: Different colors or line styles.
-   **Improved responsiveness**: Ensure the theme looks good on all device sizes.

By following these guidelines, you can help maintain and improve the `BinderPaper` theme effectively.tool_code
plan_step_complete("Created `src/themes/BinderPaper/AGENTS.md` with instructions for future agents on the theme's overview, file structure, development/testing procedures, coding conventions, and potential future enhancements.")
