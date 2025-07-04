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

# Default SITE section, includes a dynamic "Last update"
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

    # --- TEAM Section ---
    team_section_data = get_setting(pelican_object, 'HUMANS_TEAM', None)
    if team_section_data:
        humans_content.append("/* TEAM */")
        if isinstance(team_section_data, list):
            for item in team_section_data:
                if isinstance(item, dict):
                    for key, value in item.items():
                        humans_content.append(f"{key}: {value}")
                else:
                    humans_content.append(str(item))
        elif isinstance(team_section_data, dict):
            for key, value in team_section_data.items():
                humans_content.append(f"{key}: {value}")
        else: # Assumed to be a string
            humans_content.append(str(team_section_data))
    else:
        humans_content.append(DEFAULT_HUMANS_HEADER.strip())

    humans_content.append("") # Add a blank line between sections

    # --- THANKS Section ---
    thanks_section_data = get_setting(pelican_object, 'HUMANS_THANKS', None)
    if thanks_section_data:
        humans_content.append("/* THANKS */")
        if isinstance(thanks_section_data, list):
            for item in thanks_section_data:
                if isinstance(item, dict):
                    for key, value in item.items():
                        humans_content.append(f"{key}: {value}")
                else:
                    humans_content.append(str(item))
        elif isinstance(thanks_section_data, dict):
            for key, value in thanks_section_data.items():
                humans_content.append(f"{key}: {value}")
        else: # Assumed to be a string
            humans_content.append(str(thanks_section_data))
    else:
        humans_content.append(DEFAULT_HUMANS_THANKS.strip())

    humans_content.append("") # Add a blank line between sections

    # --- SITE Section ---
    site_section_data = get_setting(pelican_object, 'HUMANS_SITE', None)
    if site_section_data:
        site_content_lines = ["/* SITE */"]
        if isinstance(site_section_data, list):
            for item in site_section_data:
                if isinstance(item, dict):
                    for key, value in item.items():
                        site_content_lines.append(f"{key}: {value}")
                else:
                    site_content_lines.append(str(item))
        elif isinstance(site_section_data, dict):
            for key, value in site_section_data.items():
                site_content_lines.append(f"{key}: {value}")
        else: # Assumed to be a string
            site_content_lines.append(str(site_section_data))

        # Ensure "Last update" is present and correctly formatted.
        # Remove any existing "Last update" from custom data to avoid duplicates.
        site_content_lines = [line for line in site_content_lines if not line.lower().startswith("last update:")]
        site_content_lines.append(f"Last update: {datetime.now().strftime('%Y/%m/%d')}")
        humans_content.extend(site_content_lines)
    else:
        # Use default if no custom data; DEFAULT_HUMANS_SITE already includes "Last update".
        humans_content.append(DEFAULT_HUMANS_SITE.strip())

    # Ensure there's a blank line before the actual content if the file is not empty,
    # and ensure a single trailing newline for the file.
    final_output = "\n".join(humans_content).strip()
    if final_output: # Avoid writing just a newline if content is empty (should not happen with defaults)
        final_output += "\n"

    try:
        with open(humans_path, "w", encoding="utf-8") as f:
            f.write(final_output)
        logger.info(f"Generated humans.txt at {humans_path}")
    except Exception as e:
        logger.error(f"Could not write humans.txt: {e}")

def register():
    """Register the plugin signals."""
    signals.finalized.connect(generate_humans_txt)
