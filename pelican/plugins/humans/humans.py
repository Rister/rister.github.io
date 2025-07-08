# Copyright (c) 2024 Jeremy Rist. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see https://opensource.org/licenses/MIT.

# -*- coding: utf-8 -*-
from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path

from pelican import Pelican, signals

logger = logging.getLogger(__name__)

DEFAULT_HUMANS_HEADER = """\
/* TEAM */
Your title: Your Name.
Site: Your site
"""

DEFAULT_HUMANS_THANKS = """\
/* THANKS */
"""

DEFAULT_HUMANS_SITE = f"""\
/* SITE */
Last update: {datetime.now(timezone.utc).strftime("%Y/%m/%d")}
Standards: HTML5, CSS3
Components: Pelican
Software: Python
"""


def get_setting(pelican_object: Pelican, key: str, default: str | None = None) -> str:
    """Get a setting from the Pelican object."""
    return pelican_object.settings.get(key, default)


def _format_section_content(
    data: str | list[str | dict[str, str]] | dict[str, str]
) -> list[str]:
    """Format the content for a section in humans.txt."""
    content = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                content.append(", ".join(f"{k}: {v}" for k, v in item.items()))
            else:
                content.append(str(item))
    elif isinstance(data, dict):
        for key, value in data.items():
            content.append(f"{key}: {value}")
    else:
        content.append(str(data))
    return content


def generate_humans_txt(pelican_object: Pelican) -> None:
    """Generate the humans.txt file."""
    output_path = Path(pelican_object.output_path)
    humans_path = output_path / "humans.txt"

    humans_content = []

    # --- TEAM Section ---
    team_section_data = get_setting(pelican_object, "HUMANS_TEAM")
    if team_section_data:
        humans_content.append("/* TEAM */")
        humans_content.extend(_format_section_content(team_section_data))
    else:
        humans_content.append(DEFAULT_HUMANS_HEADER.strip())

    humans_content.append("")

    # --- THANKS Section ---
    thanks_section_data = get_setting(pelican_object, "HUMANS_THANKS")
    if thanks_section_data:
        humans_content.append("/* THANKS */")
        humans_content.extend(_format_section_content(thanks_section_data))
    else:
        humans_content.append(DEFAULT_HUMANS_THANKS.strip())

    humans_content.append("")

    # --- SITE Section ---
    site_section_data = get_setting(pelican_object, "HUMANS_SITE")
    if site_section_data:
        site_content_lines = ["/* SITE */"]
        site_content_lines.extend(_format_section_content(site_section_data))

        # Remove any existing "Last update" from custom data to avoid duplicates.
        site_content_lines = [
            line
            for line in site_content_lines
            if not line.lower().startswith("last update:")
        ]
        site_content_lines.append(
            f'Last update: {datetime.now(timezone.utc).strftime("%Y/%m/%d")}'
        )
        humans_content.extend(site_content_lines)
    else:
        humans_content.append(DEFAULT_HUMANS_SITE.strip())

    # Join all content and ensure a single trailing newline for the file.
    final_output = "\n".join(humans_content).strip()
    if final_output:
        final_output += "\n"

    try:
        humans_path.write_text(final_output, encoding="utf-8")
        logger.info("Generated humans.txt at %s", humans_path)
    except OSError:
        logger.exception("Could not write humans.txt")


def register() -> None:
    """Register the plugin signals."""
    signals.finalized.connect(generate_humans_txt)
