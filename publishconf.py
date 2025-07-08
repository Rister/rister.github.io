# Copyright (c) 2024 Jeremy Rist. All rights reserved.
#
# This work is licensed under the terms of the MIT license.
# For a copy, see https://opensource.org/licenses/MIT.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F403

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://rister.github.io"  # Update this to your actual domain
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None  # Workaround for Pelican TypeError at __init__.py:683

DELETE_OUTPUT_DIRECTORY = True
