# Copyright (c) 2024 Jeremy Rist. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see https://opensource.org/licenses/MIT.

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from pelican import Pelican
from pelican.settings import DEFAULT_CONFIG

try:
    from pelican.plugins.humans.humans import generate_humans_txt
except ImportError:
    # Fallback for running tests directly, ensuring the plugin is in the path
    # Add the 'pelican/plugins' directory to the Python path
    plugin_path = Path(__file__).parent / "pelican/plugins"
    if str(plugin_path) not in sys.path:
        sys.path.append(str(plugin_path))

    from humans.humans import generate_humans_txt


class TestHumansPlugin(unittest.TestCase):
    """Tests for the humans.txt plugin."""

    def setUp(self) -> None:
        """Set up the test environment."""
        self.temp_output_dir = Path(tempfile.mkdtemp())
        self.settings = DEFAULT_CONFIG.copy()
        self.settings["OUTPUT_PATH"] = self.temp_output_dir
        self.settings["PATH"] = "content"  # Dummy content path
        self.settings["SITEURL"] = "http://localhost"

    def tearDown(self) -> None:
        """Tear down the test environment."""
        shutil.rmtree(self.temp_output_dir)

    def _get_pelican_object(self, override_settings: dict | None = None) -> Pelican:
        """Create a Pelican object with overridden settings."""
        settings = self.settings.copy()
        if override_settings:
            settings.update(override_settings)
        return Pelican(settings)

    def test_default_humans_txt_generation(self) -> None:
        """Test default humans.txt generation."""
        pelican_obj = self._get_pelican_object()
        generate_humans_txt(pelican_obj)

        humans_file_path = self.temp_output_dir / "humans.txt"
        assert humans_file_path.exists()

        with humans_file_path.open(encoding="utf-8") as f:
            content = f.read()

        assert "/* TEAM */" in content
        assert "/* THANKS */" in content
        assert "/* SITE */" in content
        assert (
            f"Last update: {datetime.now(timezone.utc).strftime('%Y/%m/%d')}" in content
        )
        assert "Standards: HTML5, CSS3" in content
        assert "Components: Pelican" in content
        assert "Software: Python" in content

    def test_custom_team_list_generation(self) -> None:
        """Test custom team list generation."""
        custom_settings = {
            "HUMANS_TEAM": [
                "Lead Developer: Jules Verne",
                "Support: Phileas Fogg",
            ],
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = self.temp_output_dir / "humans.txt"
        with humans_file_path.open(encoding="utf-8") as f:
            content = f.read()

        assert "/* TEAM */" in content
        assert "Lead Developer: Jules Verne" in content
        assert "Support: Phileas Fogg" in content
        assert "Default Team Member" not in content

    def test_custom_team_dict_generation(self) -> None:
        """Test custom team dict generation."""
        custom_settings = {
            "HUMANS_TEAM": {
                "Project Lead": "Captain Nemo",
                "Mascot": "Nautilus",
            },
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = self.temp_output_dir / "humans.txt"
        with humans_file_path.open(encoding="utf-8") as f:
            content = f.read()

        assert "/* TEAM */" in content
        assert "Project Lead: Captain Nemo" in content
        assert "Mascot: Nautilus" in content

    def test_custom_thanks_list_generation(self) -> None:
        """Test custom thanks list generation."""
        custom_settings = {
            "HUMANS_THANKS": [
                "BigFramework Team - For their awesome framework",
                "CoffeeShop - For the endless supply of caffeine",
            ],
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = self.temp_output_dir / "humans.txt"
        with humans_file_path.open(encoding="utf-8") as f:
            content = f.read()

        assert "/* THANKS */" in content
        assert "BigFramework Team - For their awesome framework" in content
        assert "CoffeeShop - For the endless supply of caffeine" in content

    def test_custom_site_dict_generation(self) -> None:
        """Test custom site dict generation."""
        custom_settings = {
            "HUMANS_SITE": {
                "Language": "en-US",
                "Doctype": "HTML5",
                "IDE": "VS Code",
            },
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = self.temp_output_dir / "humans.txt"
        with humans_file_path.open(encoding="utf-8") as f:
            content = f.read()

        assert "/* SITE */" in content
        assert "Language: en-US" in content
        assert "Doctype: HTML5" in content
        assert "IDE: VS Code" in content
        assert (
            f"Last update: {datetime.now(timezone.utc).strftime('%Y/%m/%d')}" in content
        )

    def test_mixed_custom_and_default_generation(self) -> None:
        """Test mixed custom and default generation."""
        custom_settings = {
            "HUMANS_TEAM": [
                {"Role": "Lead Developer", "Name": "Alice Wonderland"},
                {"Role": "Content Creator", "Name": "Bob The Builder"},
                "A general contributor: Charlie Brown",
            ],
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = self.temp_output_dir / "humans.txt"
        with humans_file_path.open(encoding="utf-8") as f:
            content = f.read().strip()

        assert "Role: Lead Developer, Name: Alice Wonderland" in content
        assert "Role: Content Creator, Name: Bob The Builder" in content
        assert "A general contributor: Charlie Brown" in content

        # Ensure the section header is there
        assert content.startswith("/* TEAM */")


if __name__ == "__main__":
    unittest.main()
