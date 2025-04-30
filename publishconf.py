#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import * 

# This file contains overrides for the PRODUCTION build

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://twinkohub.netlify.app' # Make sure this matches your actual production URL
RELATIVE_URLS = False

# Enable specific feeds for production if desired (overrides pelicanconf.py)
# Keep these consistent with pelicanconf.py unless you specifically want different feeds in production
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful for production debugging:
# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
