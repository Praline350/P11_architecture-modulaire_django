# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


import os
import sys

import django


sys.path.insert(0, os.path.abspath("../../"))  # For discovery of Python modules
sys.path.insert(
    0, os.path.abspath("../../oc_lettings_site/")
)  # For finding the django_settings.py file

# This tells Django where to find the settings file
os.environ["DJANGO_SETTINGS_MODULE"] = "oc_lettings_site.settings"
# This activates Django and makes it possible for Sphinx to
# autodoc your project
django.setup()

project = "OC_lettings"
copyright = "2024, Edwin"
author = "Edwin"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    "sphinx.ext.autodoc",  # Pour extraire la documentation des docstrings
    "sphinx.ext.napoleon",  # Pour supporter les formats de docstrings Google et NumPy
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
