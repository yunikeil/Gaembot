import os
import sys
import sphinx_rtd_theme


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, "src")))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GaemBot'
copyright = '2023, yunikeil'
author = 'yunikeil'
release = '0.7'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.intersphinx', 
	'sphinx.ext.autodoc', 
	'sphinx.ext.doctest',
	'sphinx.ext.todo',
]


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autodoc_mock_imports = ['bs4', 'requsts', 'pillow']


language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
