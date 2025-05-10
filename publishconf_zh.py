#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file contains settings for the PRODUCTION Chinese site
import os
import sys

# Add current directory to the path to import pelicanconf_zh
sys.path.append(os.curdir)
# pylint: disable=wildcard-import,unused-wildcard-import
from pelicanconf_zh import *  # noqa

# Detect environment
PELICAN_ENV = os.getenv('PELICAN_ENV', 'production')

# Environment-specific settings
if PELICAN_ENV == 'production':
    SITEURL = 'https://hub.twinko.ai/zh'
elif PELICAN_ENV == 'preview':
    # For Netlify deploy previews
    if os.getenv('DEPLOY_PRIME_URL'):
        SITEURL = os.getenv('DEPLOY_PRIME_URL') + '/zh'
    else:
        SITEURL = 'https://preview.hub.twinko.ai/zh'
elif PELICAN_ENV == 'staging':
    # For branch deploys
    if os.getenv('DEPLOY_URL'):
        SITEURL = os.getenv('DEPLOY_URL') + '/zh'
    else:
        SITEURL = 'https://staging.hub.twinko.ai/zh'
else:
    # Fallback to production
    SITEURL = 'https://hub.twinko.ai/zh'

# Always use absolute URLs in production environments
RELATIVE_URLS = False

# Do not delete output directory to preserve English site files
DELETE_OUTPUT_DIRECTORY = False

# Enable Google Analytics in production
if PELICAN_ENV == 'production':
    GOOGLE_ANALYTICS = os.getenv('GOOGLE_ANALYTICS')
else:
    GOOGLE_ANALYTICS = None 