# Twinkohub Theme

A modern, responsive theme for the Twinko AI Knowledge Hub.

## Features

- Clean, modern design for knowledge hubs and blogs
- Responsive layout that works on all devices
- Optimized for readability and usability
- Customizable sidebar with categories, tags, and newsletter subscription
- Support for multi-language content
- SEO-friendly structure
- Newsletter template

## Directory Structure

- **templates/** - Jinja2 templates
  - **includes/** - Reusable template components
    - `article_list.html` - Reusable article listing with pagination
    - `sidebar.html` - Reusable sidebar with categories, tags, and forms
  - `base.html` - Base template with header and footer
  - `index.html` - Homepage template
  - `blog.html` - Blog listing template
  - `article.html` - Single article template
  - `page.html` - Static page template
  - `category.html` - Category listing template
  - `tag.html` - Tag listing template
  - `author.html` - Author listing template
  - `archives.html` - Archives template
  - `newsletter.html` - Newsletter template

- **static/** - Static assets
  - **css/** - Stylesheets
    - `style.css` - Main stylesheet
  - **images/** - Images
    - `logo.png` - Main logo
    - `logo-footer.png` - Footer logo
    - `favicon.ico` - Favicon

## Usage

To use this theme, set the following in your Pelican configuration:

```python
THEME = 'themes/twinkohub'

# Theme-specific settings
LOGO = '/theme/images/logo.png'
LOGO_FOOTER = '/theme/images/logo-footer.png'
```

## Customization

The theme supports the following additional configuration options:

- `SHOW_NEWSLETTER_FORM` - Set to True to display newsletter subscription form in sidebar
- `DEFAULT_ARTICLE_IMAGE` - Default image for articles without a specific image
- `COPYRIGHT_YEAR` - Year to display in copyright notice

## Development

This theme follows best practices for maintainability:
- DRY (Don't Repeat Yourself) principles with reusable template includes
- Clean separation of concerns between structure, presentation, and behavior
- Mobile-first responsive design
- Semantic HTML5 markup

When extending this theme, please:
1. Use the existing template includes for consistency
2. Keep CSS organized in the main stylesheet
3. Document any new features or changes 