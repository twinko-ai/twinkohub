"""
Category Translations Plugin for Pelican
=======================================

This plugin allows for mapping between display names and URL-friendly slugs
for categories, particularly useful for non-Latin languages like Chinese.
"""

from pelican import signals


def map_category_slug(category_instance):
    """Map category name to a URL-friendly slug using CATEGORY_TRANSLATIONS"""
    if not hasattr(category_instance, '_content'):
        return
    
    # Get the settings from pelican
    settings = category_instance.settings
    
    # Check if CATEGORY_TRANSLATIONS is defined in the settings
    if not hasattr(settings, 'CATEGORY_TRANSLATIONS'):
        return
    
    # Get the mapping dictionary
    translations = settings.CATEGORY_TRANSLATIONS
    
    # Check for direct match
    if category_instance.name in translations:
        category_instance.slug = translations[category_instance.name]
        return
    
    # Also check for category names that might be part of a pipe-separated string
    # For cases where the subcategory_processor hasn't run yet
    for trans_key, trans_value in translations.items():
        # Check if this category starts with one of our translatable keys followed by a pipe
        if category_instance.name.startswith(trans_key + ' |') or category_instance.name.startswith(trans_key + '｜'):
            # Set the slug based on the translation for the main category
            category_instance.slug = trans_value
            return


def process_categories(generator):
    """Process all categories with our translation mapping"""
    for category, _ in generator.categories:
        map_category_slug(category)
    # Also ensure every article's category is mapped
    for article in getattr(generator, 'articles', []):
        if hasattr(article, 'category') and article.category:
            map_category_slug(article.category)


def register():
    """Register the plugin with Pelican"""
    # Use the pretaxonomy signal to ensure mapping is done before output paths are set
    signals.article_generator_pretaxonomy.connect(process_categories) 