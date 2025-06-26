# -*- coding: utf-8 -*-
import logging
import os
from datetime import datetime

from pelican import signals

logger = logging.getLogger(__name__)

DEFAULT_HUMANS_HEADER = """\
/* TEAM */
"""

DEFAULT_HUMANS_THANKS = """\
/* THANKS */
"""

DEFAULT_HUMANS_SITE = f"""\
/* SITE */
Last update: {datetime.now().strftime('%Y/%m/%d')}
Standards: HTML5, CSS3
Components: Pelican
Software: Python
"""

def get_setting(pelican_object, key, default=None):
    """Helper function to get a setting from the Pelican object."""
    return pelican_object.settings.get(key, default)

def generate_humans_txt(pelican_object):
    """Generate the humans.txt file."""
    output_path = pelican_object.output_path
    humans_path = os.path.join(output_path, "humans.txt")

    humans_content = []

    # Get custom data from settings or use defaults
    team_section = get_setting(pelican_object, 'HUMANS_TEAM', None)
    if team_section:
        humans_content.append("/* TEAM */")
        if isinstance(team_section, list):
            for item in team_section:
                humans_content.append(str(item))
        elif isinstance(team_section, dict):
            for key, value in team_section.items():
                humans_content.append(f"{key}: {value}")
        else:
            humans_content.append(str(team_section))
    else:
        humans_content.append(DEFAULT_HUMANS_HEADER.strip())

    humans_content.append("") # Add a blank line

    thanks_section = get_setting(pelican_object, 'HUMANS_THANKS', None)
    if thanks_section:
        humans_content.append("/* THANKS */")
        if isinstance(thanks_section, list):
            for item in thanks_section:
                humans_content.append(str(item))
        elif isinstance(thanks_section, dict):
            for key, value in thanks_section.items():
                humans_content.append(f"{key}: {value}")
        else:
            humans_content.append(str(thanks_section))
    else:
        humans_content.append(DEFAULT_HUMANS_THANKS.strip())

    humans_content.append("") # Add a blank line

    site_section = get_setting(pelican_object, 'HUMANS_SITE', None)
    custom_site_info = []
    if site_section:
        custom_site_info.append("/* SITE */")
        if isinstance(site_section, list):
            for item in site_section:
                custom_site_info.append(str(item))
        elif isinstance(site_section, dict):
            for key, value in site_section.items():
                custom_site_info.append(f"{key}: {value}")
        else:
            custom_site_info.append(str(site_section))
        # Ensure Last update is present
        if not any("Last update" in line for line in custom_site_info):
            custom_site_info.append(f"Last update: {datetime.now().strftime('%Y/%m/%d')}")
        humans_content.extend(custom_site_info)
    else:
        humans_content.append(DEFAULT_HUMANS_SITE.strip())


    try:
        with open(humans_path, "w", encoding="utf-8") as f:
            f.write("\n".join(humans_content))
        logger.info(f"Generated humans.txt at {humans_path}")
    except Exception as e:
        logger.error(f"Could not write humans.txt: {e}")

def register():
    """Register the plugin signals."""
    signals.finalized.connect(generate_humans_txt)
