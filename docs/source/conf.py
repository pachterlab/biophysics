# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Pachter Lab Biophysics'
copyright = '2024, Pachter Lab'
author = 'Pachter Lab Members'

release = '0.1'
version = '0.1.0'

# -- General configuration
extensions = ["myst_parser", 
              "sphinx_design",
            'sphinx.ext.duration',
            'sphinx.ext.doctest',
            'sphinx.ext.autodoc',
            'sphinx.ext.autosummary',
            'sphinx.ext.intersphinx'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

#### sphinx ####

myst_enable_extensions = ["colon_fence", "deflist", "substitution", "html_image"]
