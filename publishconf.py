#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file contains ALL settings for the PRODUCTION build
import datetime
import os

# Basic Settings
AUTHOR = 'Twinko AI'
SITENAME = 'Twinko AI Knowledge Hub'

# Detect environment
PELICAN_ENV = os.getenv('PELICAN_ENV', 'production')

# Environment-specific settings
if PELICAN_ENV == 'production':
    SITEURL = 'https://hub.twinko.ai'
elif PELICAN_ENV == 'preview':
    # For Netlify deploy previews
    if os.getenv('DEPLOY_PRIME_URL'):
        SITEURL = os.getenv('DEPLOY_PRIME_URL')
    else:
        SITEURL = 'https://preview.hub.twinko.ai'
elif PELICAN_ENV == 'staging':
    # For branch deploys
    if os.getenv('DEPLOY_URL'):
        SITEURL = os.getenv('DEPLOY_URL')
    else:
        SITEURL = 'https://staging.hub.twinko.ai'
else:
    # Fallback to production
    SITEURL = 'https://hub.twinko.ai'

# Always use absolute URLs in production environments
RELATIVE_URLS = False

# Delete output directory before generating new files
DELETE_OUTPUT_DIRECTORY = True

# Path Configuration
PATH = "content"
PLUGIN_PATHS = ['plugins']
PLUGINS = ['subcategory_processor']

ARTICLE_PATHS = ['en/blog', 'en/newsletter']
PAGE_PATHS = ['en/pages']
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
THEME = 'themes/twinkohub'

# Theme-specific settings
LOGO = '/theme/images/logo.png'
LOGO_FOOTER = '/theme/images/logo-footer.png'

# URL settings - updated to use path instead of category
ARTICLE_URL = '{path}/{slug}.html'
ARTICLE_SAVE_AS = '{path}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Use the filename as slug for newsletter articles to prevent nested folders
SLUGIFY_SOURCE = 'basename'  # Use filename instead of title for slug
PATH_METADATA = '(?P<path>.*)/(?P<slug>.*)\.md'

# Categories and tags settings
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Index page settings
INDEX_SAVE_AS = 'index.html'

# Blog and Newsletter settings
DIRECT_TEMPLATES = [
    'index', 'categories', 'archives', 'tags', 'authors', 
    'blog', 'newsletter', 'newsfeed'
]
BLOG_URL = 'blog/'
BLOG_SAVE_AS = 'blog/index.html'
NEWSLETTER_URL = 'newsletter/'
NEWSLETTER_SAVE_AS = 'newsletter/index.html'
NEWSFEED_URL = 'newsfeed/'
NEWSFEED_SAVE_AS = 'newsfeed/index.html'

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

# Markdown extensions for proper heading IDs and TOC
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'permalink': False,
            'toc_depth': '2-3'
        },
    },
    'output_format': 'html5',
}

# Feed settings
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
FEED_ATOM = None
FEED_RSS = None
NEWSLETTER_FEED_ATOM = 'feeds/newsletter.atom.xml'
NEWSLETTER_FEED_RSS = 'feeds/newsletter.rss.xml'
BLOG_FEED_ATOM = 'feeds/blog.atom.xml'
BLOG_FEED_RSS = 'feeds/blog.rss.xml'

# RSS Feed Widget IDs - Use environment variables
RSS_FEED_IDS = {
    'everything': os.getenv('RSS_FEED_ID_EVERYTHING'),
    'healthcare': os.getenv('RSS_FEED_ID_HEALTHCARE'),
    'agents': os.getenv('RSS_FEED_ID_AGENTS'),
    'bioinformatics': os.getenv('RSS_FEED_ID_BIOINFORMATICS'),
    'safety': os.getenv('RSS_FEED_ID_SAFETY'),
    'homepage_carousel': os.getenv('RSS_FEED_ID_HOMEPAGE_CAROUSEL')
}

# Enable Google Analytics only in production
if PELICAN_ENV == 'production':
    GOOGLE_ANALYTICS = os.getenv('GOOGLE_ANALYTICS')
else:
    GOOGLE_ANALYTICS = None
