#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file contains settings for Chinese LOCAL development
import datetime
import os

# Basic Settings
AUTHOR = 'Twinko AI'
SITENAME = 'Twinko AI 知识中心'

# Local development settings
SITEURL = 'http://localhost:8000/zh'
RELATIVE_URLS = True

# Path Configuration
PATH = "content"
# Remove OUTPUT_PATH (let Pelican use the default output/)
PLUGIN_PATHS = ['plugins']
# Use our custom Chinese-specific category processor
PLUGINS = ['zh_category_processor']

# Content paths specifically for Chinese
ARTICLE_PATHS = ['zh/blog', 'zh/newsletter']
PAGE_PATHS = ['zh/pages']
STATIC_PATHS = ['images', 'extra']

# Ensure 404.html is copied to the output directory root
EXTRA_PATH_METADATA = {
    'extra/404.html': {'path': '404.html'},
}

# Default language (Chinese)
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh'
THEME = 'themes/twinkohub_zh'
THEME_STATIC_DIR = 'theme'

# Output base path for Chinese site
OUTPUT_PATH_BASE = 'zh'

# Chinese templates - direct indexing
INDEX_TEMPLATE = 'index_zh.html'
DIRECT_TEMPLATES = [
    'index', 'categories', 'archives', 'tags', 'authors', 
    'blog', 'newsletter', 'newsfeed'
]

# Theme-specific settings
LOGO = '/theme/images/logo.png'
LOGO_FOOTER = '/theme/images/logo-footer.png'

# URL settings 
ARTICLE_URL = 'zh/{path}/{slug}.html'
ARTICLE_SAVE_AS = 'zh/{path}/{slug}.html'
PAGE_URL = 'zh/{slug}.html'
PAGE_SAVE_AS = 'zh/{slug}.html'

# Use filename as slug for newsletter articles to prevent nested folders
SLUGIFY_SOURCE = 'basename'  # Use filename instead of title for slug
PATH_METADATA = '(?P<path>.*)/(?P<slug>.*)\.md'

# Categories and tags settings
CATEGORY_URL = 'zh/category/{slug}/'
CATEGORY_SAVE_AS = 'zh/category/{slug}/index.html'
TAG_URL = 'zh/tag/{slug}/'
TAG_SAVE_AS = 'zh/tag/{slug}/index.html'

# Index page settings - output as Chinese home
INDEX_SAVE_AS = 'zh/index.html'

# Blog and Newsletter settings
BLOG_URL = 'zh/blog/'
BLOG_SAVE_AS = 'zh/blog/index.html'
NEWSLETTER_URL = 'zh/newsletter/'
NEWSLETTER_SAVE_AS = 'zh/newsletter/index.html'
NEWSFEED_URL = 'zh/newsfeed/'
NEWSFEED_SAVE_AS = 'zh/newsfeed/index.html'

# Archives, authors, categories, tags
ARCHIVES_SAVE_AS = 'zh/archives.html'
AUTHORS_SAVE_AS = 'zh/authors.html'
CATEGORIES_SAVE_AS = 'zh/categories.html'
TAGS_SAVE_AS = 'zh/tags.html'
AUTHOR_URL = 'zh/author/{slug}/'
AUTHOR_SAVE_AS = 'zh/author/{slug}/index.html'

# Chinese category mappings (display name to URL-friendly slug)
CATEGORY_TRANSLATIONS = {
    '行业AI周刊': 'twinko-weekly',  # Human-readable to URL slug
}

# Translation strings
TRANSLATIONS = {
    'Home': '首页',
    'Newsfeed': '新闻动态',
    'Newsletter': '周报',
    'Blog': '博客',
    'Subscribe': '订阅',
    'Archives': '归档',
    'Categories': '分类',
    'Tags': '标签',
    'Content': '内容',
    'Company': '公司',
    'About Us': '关于我们',
    'Our Team': '团队',
    'Contact': '联系我们',
    'Follow Us': '关注我们',
}

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
NEWSLETTER_FEED_ATOM = 'zh/feeds/newsletter.atom.xml'
NEWSLETTER_FEED_RSS = 'zh/feeds/newsletter.rss.xml'
BLOG_FEED_ATOM = 'zh/feeds/blog.atom.xml'
BLOG_FEED_RSS = 'zh/feeds/blog.rss.xml'

# RSS Feed Widget IDs - Use environment variables
RSS_FEED_IDS = {
    'everything': os.getenv('RSS_FEED_ID_EVERYTHING_ZH'),
    'healthcare': os.getenv('RSS_FEED_ID_HEALTHCARE_ZH'),
    'agents': os.getenv('RSS_FEED_ID_AGENTS_ZH'),
    'bioinformatics': os.getenv('RSS_FEED_ID_BIOINFORMATICS_ZH'),
    'safety': os.getenv('RSS_FEED_ID_SAFETY_ZH'),
    'homepage_carousel': os.getenv('RSS_FEED_ID_HOMEPAGE_CAROUSEL_ZH')
}

# Disable Google Analytics for local development
GOOGLE_ANALYTICS = None

# Don't delete the output directory on rebuild for local development
DELETE_OUTPUT_DIRECTORY = False 