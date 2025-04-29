from pelicanconf import *

# Remove hardcoded URL to make it work with Netlify's domain
SITEURL = ''
RELATIVE_URLS = True

# Feed settings
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
