import pathlib
import sys
import os
print(os.path.abspath('../../../'))  # Add this line to conf.py and run make html
sys.path.insert(0, os.path.abspath('../../../'))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'utcxchangelib'
copyright = '2025, UChicagoFM'
author = 'UChicagoFM'
release = '0.1.1'
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',         # Generates API docs from docstrings
    'sphinx.ext.napoleon',        # Supports Google and NumPy style docstrings
    # 'sphinx.ext.autosummary',     # Generates summary pages
    'sphinx.ext.viewcode',        # Adds source code links (recommended)
    'sphinx.ext.intersphinx',     # Links to other project's documentation
    'sphinx.ext.duration',
    'sphinx_rtd_theme',
]

autosummary_generate = True
autodoc_mock_imports = ["requests"]  # Mock external dependencies

# Napoleon settings to process Google-style docstrings correctly
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Theme: Read the Docs style
html_static_path = ['_static']  # Path for custom static files

# -- Source code linking options ---------------------------------------------
# Viewcode allows each function/class to be linked to its source code
# Enabling it adds [source] links to class/function definitions
