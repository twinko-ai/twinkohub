# Template Includes

This directory contains reusable template components that are included in multiple templates to reduce code duplication and improve maintainability.

## Available Includes

### article_list.html

Displays a list of articles with pagination. Used in:
- category.html
- tag.html
- author.html
- blog.html

### sidebar.html

Displays the sidebar with categories, tags, and optionally a newsletter subscription form. Used in:
- category.html
- tag.html
- author.html
- blog.html
- newsletter.html

## Usage

To use an include in a template:

```jinja2
{% include 'includes/article_list.html' %}
```

For the sidebar with an active category:

```jinja2
{% set active_category = category %}
{% include 'includes/sidebar.html' %}
```

To show the newsletter form in the sidebar:

```jinja2
{% set SHOW_NEWSLETTER_FORM = True %}
{% include 'includes/sidebar.html' %}
``` 