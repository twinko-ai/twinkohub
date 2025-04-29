#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or explicitly specify it as your config file.

from pelicanconf import *

# Production URL
SITEURL = 'https://twinkohub.netlify.app'
RELATIVE_URLS = False

# Feed settings
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

# Delete output directory before generating new files
DELETE_OUTPUT_DIRECTORY = True
