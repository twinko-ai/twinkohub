#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file contains ALL settings for the PRODUCTION build
import datetime

# --- Settings from pelicanconf.py --- 
AUTHOR = 'Twinko AI'
SITENAME = 'Twinko AI Knowledge Hub'

PATH = "content"
PLUGIN_PATHS = ['plugins']
PLUGINS = []

ARTICLE_PATHS = ['en/blog', 'en/newsletter']
PAGE_PATHS = ['en/pages']
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
THEME = 'themes/twinkohub'

# Theme-specific settings
LOGO = '/theme/images/logo.png'
LOGO_FOOTER = '/theme/images/logo-footer.png'

# URL settings
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Categories and tags settings
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Index page settings
INDEX_SAVE_AS = 'index.html'

# Blog and Newsletter settings
DIRECT_TEMPLATES = [
    'index', 'categories', 'archives', 'tags', 'authors', 'blog', 'newsletter'
]
BLOG_URL = 'blog/'
BLOG_SAVE_AS = 'blog/index.html'
NEWSLETTER_URL = 'newsletter/'
NEWSLETTER_SAVE_AS = 'newsletter/index.html'

# Social links for footer
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/company/twinko-ai"),
    ("GitHub", "https://github.com/twinko-ai"),
    ("Twitter", "https://x.com/TwinkoAI")
)

# Default pagination
DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 150

# Theme-specific extras
DEFAULT_ARTICLE_IMAGE = 'theme/images/default-article.jpg'
COPYRIGHT_YEAR = datetime.date.today().year

# --- Production-specific settings --- 
SITEURL = 'https://twinkohub.netlify.app'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
