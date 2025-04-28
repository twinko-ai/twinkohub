# Twinko Hub Theme

A modern, responsive theme for the Twinko AI Hub Pelican website. This theme is designed to match the style and layout of the main Twinko AI website.

## Features

- Responsive design for mobile, tablet, and desktop
- Support for multi-language content with i18n_subsites
- Blog post listings with featured images
- Category and tag pages
- Article archives
- Author pages
- Clean and modern styling

## Requirements

- Pelican 4.5+
- i18n_subsites plugin

## Configuration

The theme can be configured with the following settings in your `pelicanconf.py`:

```python
# Theme-specific settings
LOGO = '/theme/images/logo.png'
LOGO_FOOTER = '/theme/images/logo-footer.png'

# Social widget - Format: (Name, URL)
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/company/twinko-ai"),
    ("GitHub", "https://github.com/twinko-ai"),
    ("Twitter", "https://x.com/TwinkoAI")
)

# Content summary settings
SUMMARY_MAX_LENGTH = 150

# Default article image if none is provided
DEFAULT_ARTICLE_IMAGE = 'theme/images/default-article.jpg'
```

## Usage

To use this theme, set the following in your `pelicanconf.py`:

```python
THEME = 'themes/twinkohub'
```

### Adding Images to Articles

Add images to your articles with the `image` metadata:

```markdown
Title: My Article Title
Date: 2023-10-15
Category: News
Tags: pelican, theme
Authors: Author Name
image: images/my-article-image.jpg

Article content here...
```

## Credits

Created for Twinko AI by the Twinko AI team. 