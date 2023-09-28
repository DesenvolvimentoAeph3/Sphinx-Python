# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Projeto1'
copyright = '2023, Eng G.Locateli'
author = 'Eng G.Locateli'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages"
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt-BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output




html_theme = 'sphinx_rtd_theme'
html_theme_path = sphinx_rtd_theme.get_html_theme_path()
html_static_path = ["_static"]