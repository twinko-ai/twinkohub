"""
Subcategory Processor
====================

This plugin processes hierarchical category strings like "Twinko Weekly | Healthcare"
into main categories and subcategories.
"""

from pelican import signals
from pelican.contents import Article
from pelican.urlwrappers import Category


def extract_subcategory(article_generator):
    """
    Process articles to extract main categories and subcategories
    from format like "Main Category | Subcategory"
    """
    # Create a dictionary to track existing parent categories
    parent_categories = {}
    
    for article in article_generator.articles:
        if hasattr(article, 'category') and article.category and '|' in article.category.name:
            # Split the category into main and sub
            parts = [part.strip() for part in article.category.name.split('|', 1)]
            main_category_name = parts[0]
            subcategory_name = parts[1] if len(parts) > 1 else ''
            
            # Store the original full category
            article.full_category = article.category
            
            # Set main category and subcategory attributes
            article.main_category = main_category_name
            article.subcategory = subcategory_name
            
            # Check if we already have this parent category
            if main_category_name in parent_categories:
                # Reuse existing parent category object
                article.category = parent_categories[main_category_name]
            else:
                # Create a new Category with proper slug
                main_category = Category(main_category_name, article_generator.settings)
                # Store for reuse
                parent_categories[main_category_name] = main_category
                # Update article's category
                article.category = main_category
                
                # Add to article_generator's categories if not already there
                if main_category not in article_generator.categories:
                    article_generator.categories.append((main_category, []))
        else:
            # For articles without the pipe separator
            article.main_category = getattr(article, 'category', None)
            article.subcategory = ''
            article.full_category = getattr(article, 'category', None)

    # Update category lists to ensure all articles are in the right buckets
    for category, articles in article_generator.categories:
        article_generator.categories = [
            (cat, [article for article in article_generator.articles 
                  if article.category == cat]) 
            for cat in set(article.category for article in article_generator.articles 
                       if hasattr(article, 'category') and article.category)
        ]
    
    # Also update category_set
    article_generator.category_set = set(category for category, _ in article_generator.categories)


def register():
    """Register the plugin with Pelican"""
    signals.article_generator_finalized.connect(extract_subcategory) 