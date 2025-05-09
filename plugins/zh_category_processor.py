"""
Chinese Category Processor Plugin for Pelican
===========================================

This plugin ensures all articles with '行业AI周刊' in their category
are mapped to the slug 'twinko-weekly'.
"""

from pelican import signals
from pelican.urlwrappers import Category

ZH_WEEKLY_NAME = '行业AI周刊'
ZH_WEEKLY_SLUG = 'twinko-weekly'

def process_zh_categories(generator):
    """Process Chinese categories and map articles."""
    print("Running zh_category_processor plugin...")
    
    # First pass - just map the categories of each article
    for article in generator.articles:
        if not hasattr(article, 'category') or not article.category:
            continue
            
        cat_name = article.category.name
        print(f"Processing: {article.title[:30]}... - Category: {cat_name}")
        
        # Check if this is a twinko-weekly article (with or without spaces or subcategory)
        if ZH_WEEKLY_NAME in cat_name:
            # This is a weekly article
            print(f"  → Mapping to: {ZH_WEEKLY_SLUG}")
            
            # Extract subcategory if present
            if '|' in cat_name:
                parts = [p.strip() for p in cat_name.split('|', 1)]
                subcategory = parts[1] if len(parts) > 1 else ''
            elif '｜' in cat_name:
                parts = [p.strip() for p in cat_name.split('｜', 1)]
                subcategory = parts[1] if len(parts) > 1 else ''
            else:
                subcategory = ''
                
            # Create the category with correct slug
            category = Category(ZH_WEEKLY_NAME, generator.settings)
            category.slug = ZH_WEEKLY_SLUG
            
            # Set article attributes
            article.category = category
            article.main_category = ZH_WEEKLY_NAME
            article.subcategory = subcategory
        else:
            # This is a regular article (blog, etc.)
            print(f"  → Regular category: {cat_name}")
            article.main_category = cat_name
            article.subcategory = ''
            
    print("Chinese category processing complete.")

def register():
    signals.article_generator_pretaxonomy.connect(process_zh_categories) 