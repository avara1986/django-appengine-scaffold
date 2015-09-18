#!/usr/bin/env python
import os
import sys
from os.path import dirname, abspath, join, exists

PROJECT_DIR = (dirname(abspath('__file__')))
SITEPACKAGES_DIR = join(PROJECT_DIR, "sitepackages")
APPENGINE_DIR = join(SITEPACKAGES_DIR, "google_appengine")

if exists(APPENGINE_DIR) and APPENGINE_DIR not in sys.path:
    sys.path.insert(1, APPENGINE_DIR)

if SITEPACKAGES_DIR not in sys.path:
    sys.path.insert(1, SITEPACKAGES_DIR)

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "settings.settings_local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
