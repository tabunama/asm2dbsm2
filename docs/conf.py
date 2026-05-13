import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "ASM2d-BSM2"
author = "Taher Abunama"
copyright = "2026"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
    "sphinx_rtd_theme",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "ASM2d-BSM2"
html_short_title = "ASM2d-BSM2"
html_static_path = ["_static"]
html_theme_options = {
    "titles_only": True,
    "navigation_depth": 2,
}
