import os
import shutil
import tempfile
import unittest
from datetime import datetime

from pelican.settings import DEFAULT_CONFIG
from pelican import Pelican

# Import the plugin - this assumes it's in python path or structure allows direct import
# For a local plugin, we might need to adjust sys.path or ensure the structure is correct
# For now, assuming `pelican/plugins` is a package or can be added to path.
# A more robust way might be to use pelican's plugin loading mechanism if testing outside pelican process
try:
    from pelican.plugins.humans.humans import generate_humans_txt, register
except ImportError:
    # This is a common issue when running tests directly if plugin path isn't set up
    # For a real test suite, you'd ensure PYTHONPATH or similar is configured
    print("Failed to import plugin directly, ensure pelican.plugins.humans is in PYTHONPATH")
    # As a fallback for this specific environment, try a relative path (not ideal for robust tests)
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), 'pelican/plugins'))
    from humans.humans import generate_humans_txt, register


class TestHumansPlugin(unittest.TestCase):

    def setUp(self):
        self.temp_output_dir = tempfile.mkdtemp()
        self.settings = DEFAULT_CONFIG.copy()
        self.settings['OUTPUT_PATH'] = self.temp_output_dir
        self.settings['PATH'] = 'content' # Dummy content path
        self.settings['SITEURL'] = 'http://localhost'
        # Ensure plugin is registered for testing its signal connection if needed,
        # but here we'll call generate_humans_txt directly for simplicity.
        # register() # This would normally be called by Pelican

    def tearDown(self):
        shutil.rmtree(self.temp_output_dir)

    def _get_pelican_object(self, override_settings=None):
        settings = self.settings.copy()
        if override_settings:
            settings.update(override_settings)
        return Pelican(settings)

    def test_default_humans_txt_generation(self):
        pelican_obj = self._get_pelican_object()
        generate_humans_txt(pelican_obj)

        humans_file_path = os.path.join(self.temp_output_dir, "humans.txt")
        self.assertTrue(os.path.exists(humans_file_path))

        with open(humans_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("/* TEAM */", content)
        self.assertIn("/* THANKS */", content)
        self.assertIn("/* SITE */", content)
        self.assertIn(f"Last update: {datetime.now().strftime('%Y/%m/%d')}", content)
        self.assertIn("Standards: HTML5, CSS3", content)
        self.assertIn("Components: Pelican", content)
        self.assertIn("Software: Python", content)

    def test_custom_team_list_generation(self):
        custom_settings = {
            'HUMANS_TEAM': [
                'Lead Developer: Jules Verne',
                'Support: Phileas Fogg'
            ]
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = os.path.join(self.temp_output_dir, "humans.txt")
        with open(humans_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("/* TEAM */", content)
        self.assertIn("Lead Developer: Jules Verne", content)
        self.assertIn("Support: Phileas Fogg", content)
        self.assertNotIn("Default Team Member", content) # Assuming default might have this

    def test_custom_team_dict_generation(self):
        custom_settings = {
            'HUMANS_TEAM': {
                'Project Lead': 'Captain Nemo',
                'Mascot': 'Nautilus'
            }
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = os.path.join(self.temp_output_dir, "humans.txt")
        with open(humans_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("/* TEAM */", content)
        self.assertIn("Project Lead: Captain Nemo", content)
        self.assertIn("Mascot: Nautilus", content)

    def test_custom_thanks_list_generation(self):
        custom_settings = {
            'HUMANS_THANKS': [
                'BigFramework Team - For their awesome framework',
                'CoffeeShop - For the endless supply of caffeine'
            ]
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = os.path.join(self.temp_output_dir, "humans.txt")
        with open(humans_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("/* THANKS */", content)
        self.assertIn("BigFramework Team - For their awesome framework", content)
        self.assertIn("CoffeeShop - For the endless supply of caffeine", content)

    def test_custom_site_dict_generation(self):
        custom_settings = {
            'HUMANS_SITE': {
                'Language': 'en-US',
                'Doctype': 'HTML5',
                'IDE': 'VS Code'
            }
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = os.path.join(self.temp_output_dir, "humans.txt")
        with open(humans_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("/* SITE */", content)
        self.assertIn("Language: en-US", content)
        self.assertIn("Doctype: HTML5", content)
        self.assertIn("IDE: VS Code", content)
        self.assertIn(f"Last update: {datetime.now().strftime('%Y/%m/%d')}", content) # Should still be there

    def test_mixed_custom_and_default_generation(self):
        custom_settings = {
            'HUMANS_TEAM': [
                'The One And Only: Me'
            ]
            # HUMANS_THANKS and HUMANS_SITE will use defaults
        }
        pelican_obj = self._get_pelican_object(custom_settings)
        generate_humans_txt(pelican_obj)

        humans_file_path = os.path.join(self.temp_output_dir, "humans.txt")
        with open(humans_file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("/* TEAM */", content)
        self.assertIn("The One And Only: Me", content)

        self.assertIn("/* THANKS */", content) # Default thanks section header

        self.assertIn("/* SITE */", content) # Default site section header
        self.assertIn("Standards: HTML5, CSS3", content) # Default site content

if __name__ == '__main__':
    unittest.main()
