# Pelican Humans.txt Plugin

This plugin generates a `humans.txt` file for your Pelican site. This file can provide information about the people behind the website, the technology used, and any acknowledgments.

## Installation

1.  Ensure this plugin is accessible in your Pelican project, typically by placing the `humans` folder (containing `humans.py`, `__init__.py`, and this `README.md`) into a `plugins` directory within your Pelican project structure (e.g., `my_pelican_site/plugins/humans`).
2.  Alternatively, for more global use, you might install it as a Python package if it were structured as one. For local plugin use, the directory method is common.

## Enabling the Plugin

In your `pelicanconf.py` file, you need to tell Pelican about the plugin:

```python
# pelicanconf.py

# If your plugins are in a directory named 'plugins' at the root of your project:
PLUGIN_PATHS = ['plugins']
# Or, if you placed the 'humans' folder directly into a 'pelican/plugins' structure recognized by your PYTHONPATH:
# PLUGIN_PATHS = ['pelican/plugins'] # Adjust as per your structure

PLUGINS = ['humans'] # Use the short name of the plugin folder/module
```

If `PLUGIN_PATHS` is not specified, Pelican might still find it if the `pelican.plugins.humans` module is directly installable or discoverable in your Python environment (e.g., via `sys.path` or if it's a namespace package). However, for local plugins, explicitly setting `PLUGIN_PATHS` is the most reliable method.

## Configuration

You can customize the content of `humans.txt` by adding settings to your `pelicanconf.py`.

The following settings are available:

*   `HUMANS_TEAM`: Information about the team behind the site.
    *   Can be a list of strings.
    *   Can be a list of dictionaries (each dict is a person with key-value attributes).
    *   Can be a single string.
    *   If not provided, a default "/* TEAM */" header is used.
*   `HUMANS_THANKS`: Acknowledgments for tools, services, or individuals.
    *   Can be a list of strings.
    *   Can be a list of dictionaries.
    *   Can be a single string.
    *   If not provided, a default "/* THANKS */" header is used.
*   `HUMANS_SITE`: Information about the site itself (technology, standards, etc.).
    *   Can be a list of strings.
    *   Can be a dictionary of key-value pairs.
    *   Can be a single string.
    *   If not provided, default information including "Last update", "Standards", "Components", and "Software" is used. The "Last update" field is always automatically added to this section.

### Example Configuration

```python
# pelicanconf.py

HUMANS_TEAM = [
    {'Role': 'Lead Developer', 'Name': 'Your Name', 'Contact': 'your.email@example.com'},
    {'Role': 'Content Creator', 'Name': 'Another Person'},
    'A general contributor',
]

HUMANS_THANKS = [
    'Pelican maintainers for the great static site generator.',
    'The open-source community.',
    {'Service': 'Hosting Provider Inc.', 'For': 'Reliable hosting services'},
]

HUMANS_SITE = {
    'Language': 'English (US)',
    'Standards Compliance': 'WCAG 2.1 AA, HTML5, CSS3',
    'Primary Technology': 'Python & Pelican',
    'Hosting Environment': 'My Awesome Server',
    # 'Last update' will be added automatically by the plugin.
}
```

If any of these settings are omitted, the plugin will use sensible defaults for that section.

## Output

The plugin will generate a `humans.txt` file in the root of your site's output directory (e.g., `output/humans.txt`).

Example of a generated `humans.txt` with the configuration above:

```
/* TEAM */
Role: Lead Developer
Name: Your Name
Contact: your.email@example.com
Role: Content Creator
Name: Another Person
A general contributor

/* THANKS */
Pelican maintainers for the great static site generator.
The open-source community.
Service: Hosting Provider Inc.
For: Reliable hosting services

/* SITE */
Language: English (US)
Standards Compliance: WCAG 2.1 AA, HTML5, CSS3
Primary Technology: Python & Pelican
Hosting Environment: My Awesome Server
Last update: 2023/10/27
```
(Note: The `Last update` date will reflect the actual generation date.)

## How it Works

The plugin hooks into Pelican's `finalized` signal. This means it runs after Pelican has finished generating all other content for your site. It then gathers the configured (or default) data and writes it to the `humans.txt` file.
```
