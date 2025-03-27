# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'utcxchangelib'
copyright = '2025, Ian Magnell, Preston Thiele, Arya Vohra, Dale Ren'
author = 'Ian Magnell, Preston Thiele, Arya Vohra, Dale Ren'
release = '0.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []

language = 'Python'

extensions = [
    'sphinx.ext.autodoc',         # Generates API docs from docstrings
    'sphinx.ext.napoleon',        # Supports Google and NumPy style docstrings
    'sphinx.ext.autosummary',     # Generates summary pages
    'sphinx.ext.viewcode',        # Adds source code links (recommended)
    'sphinx.ext.intersphinx',     # Links to other project's documentation
]

# Paths for autodoc
import os
import sys
# sys.path.insert(0, os.path.dirname(os.path.abspath('../../'))) # Adjust path to root where the package lives

# Napoleon settings to process Google-style docstrings correctly
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Paths for autodoc
autosummary_generate = True
autodoc_mock_imports = ["requests"]
