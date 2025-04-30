#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# No need for sys.path manipulation if run from project root

from pelicanconf import * 

# This file contains ALL settings for the PRODUCTION build
import datetime
import os  # <<< Added os import for getenv

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://twinkohub.netlify.app' # Make sure this matches your actual production URL
RELATIVE_URLS = False

# Inherit feed settings from pelicanconf.py unless specifically overridden
# Example feed override (currently using settings from pelicanconf):
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful for production debugging:
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""

# RSS Feed Widget IDs - Use environment variables (Copied from pelicanconf)
RSS_FEED_IDS = {
    'everything': os.getenv('RSS_FEED_ID_EVERYTHING'),
    'healthcare': os.getenv('RSS_FEED_ID_HEALTHCARE'),
    'agents': os.getenv('RSS_FEED_ID_AGENTS'),
    'bioinformatics': os.getenv('RSS_FEED_ID_BIOINFORMATICS'),
    'safety': os.getenv('RSS_FEED_ID_SAFETY'),
    'homepage_carousel': os.getenv('RSS_FEED_ID_HOMEPAGE_CAROUSEL')
}
