# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Pachter Biophysics'
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

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Enable dropdown
# extensions = ["sphinx_design"]
# html_theme_options = {
#     ...
#     'navigation_with_keys': True,
#     ...
# }


html_static_path = ["_static"]
html_logo = "_static/logo_wide.svg"
html_favicon = "_static/logo_square.svg"

if html_theme not in ("sphinx_book_theme", "pydata_sphinx_theme"):
    html_css_files = [
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
    ]
if html_theme == "alabaster":
    html_logo = ""
    html_theme_options = {
        "logo": "logo_wide.svg",
        "logo_name": False,
        "description": "(alabaster theme)",
        "github_button": False,
        "github_type": "star",
        "github_banner": False,
        "github_user": "executablebooks",
        "github_repo": "sphinx-design",
    }
if html_theme == "sphinx_book_theme":
    html_theme_options = {
        "repository_url": "https://github.com/executablebooks/sphinx-design",
        "use_repository_button": True,
        "use_edit_page_button": True,
        "use_issues_button": True,
        "repository_branch": "main",
        "path_to_docs": "docs",
        "home_page_in_toc": False,
    }
if html_theme == "furo":
    html_css_files = [
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/fontawesome.min.css"
    ]
    html_theme_options = {
        "sidebar_hide_name": True,
    }
if html_theme == "sphinx_rtd_theme":
    html_theme_options = {
        "logo_only": True,
    }

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
myst_enable_extensions = ["colon_fence", "deflist", "substitution", "html_image"]


