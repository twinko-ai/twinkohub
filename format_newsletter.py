#!/usr/bin/env python3
"""
Newsletter Article Formatter

This script formats newsletter articles according to standardized rules:
1. Ensures proper line breaks (two spaces) after sources
2. Makes "Read more →" appear on its own line
3. Removes duplicate H1 headings (keeping only metadata title)
4. Makes external links open in new tabs with target="_blank"
5. Other formatting consistencies

Usage:
    python format_newsletter.py path/to/article.md  # Format single article
    python format_newsletter.py path/to/folder/     # Format all .md files
"""

import os
import re
import sys
import glob


def format_article(content):
    """
    Format article content according to the defined rules.
    
    Args:
        content (str): The original article content
        
    Returns:
        str: The formatted article content
    """
    # Replace any Windows line endings with Unix line endings
    content = content.replace('\r\n', '\n')
    
    # Extract metadata section (everything before the first blank line)
    parts = content.split('\n\n', 1)
    if len(parts) < 2:
        return content  # No metadata section found
    
    metadata = parts[0]
    article_content = parts[1]
    
    # Remove the first H1 heading from the article content
    # This prevents duplicate titles (metadata title + content H1)
    article_content = re.sub(
        r'^# .+?\n\n', '', article_content, flags=re.DOTALL
    )
    
    # Recombine metadata and content
    content = metadata + '\n\n' + article_content
    
    # Function to format news items in Twinko Weekly articles
    def format_news_item(match):
        news_item = match.group(0)
        
        # Fix issue where Date and Source aren't properly separated 
        # from description - add two spaces followed by newline
        date_source_pattern = (
            r'(\*\*Date\*\*:\s+[^\n]+\s+\*\*Source\*\*:\s+[^\n]+)'
            r'(\s+)([A-Z])'
        )
        news_item = re.sub(date_source_pattern, r'\1  \n\3', news_item)
        
        # Ensure "Read more →" is on its own line with two spaces
        # before the newline and add target="_blank"
        read_more_pattern = (
            r'([^.\n])(\s+)(\[Read more →\])\(([^)]+)\)'
        )
        news_item = re.sub(
            read_more_pattern, r'\1  \n\3(\4){: target="_blank"}', news_item
        )
        
        # Also handle case where period is followed by Read more
        read_more_pattern2 = (
            r'(\.)(\s+)(\[Read more →\])\(([^)]+)\)'
        )
        news_item = re.sub(
            read_more_pattern2, r'\1  \n\3(\4){: target="_blank"}', news_item
        )
        
        # Handle "阅读更多 →" for Chinese articles 
        read_more_zh_pattern = (
            r'([^.\n])(\s+)(\[阅读更多 →\])\(([^)]+)\)'
        )
        news_item = re.sub(
            read_more_zh_pattern, r'\1  \n\3(\4){: target="_blank"}', news_item
        )
        
        read_more_zh_pattern2 = (
            r'(\.)(\s+)(\[阅读更多 →\])\(([^)]+)\)'
        )
        news_item = re.sub(
            read_more_zh_pattern2, 
            r'\1  \n\3(\4){: target="_blank"}', 
            news_item
        )
        
        # Remove any double newlines between content and Read more links
        # and replace with two spaces and a single newline
        double_newline_pattern = r'([^\n])\n\n(\[(?:Read more|阅读更多) →\])'
        news_item = re.sub(double_newline_pattern, r'\1  \n\2', news_item)
        
        return news_item
    
    # Process each news item section (starting with ###)
    news_item_pattern = (
        r'### [^\n]+\n\n(?:(?!###).)+?(?=\n\n### |\n*$)'
    )
    content = re.sub(
        news_item_pattern, format_news_item, content, flags=re.DOTALL
    )
    
    # Add target="_blank" to all external links that don't already have it
    # Match Markdown links with http(s) URLs
    link_text = r'\[([^\]]+)\]'
    http_url = r'\((https?://[^)]+)\)'
    not_attributed = r'(?!\{:)'
    external_link_pattern = link_text + http_url + not_attributed
    
    content = re.sub(
        external_link_pattern, 
        r'[\1](\2){: target="_blank"}', 
        content
    )
    
    # Ensure there are two newlines after each heading
    heading_pattern = r'(#+ [^\n]+)\n(?!\n)'
    content = re.sub(heading_pattern, r'\1\n\n', content)
    
    # Remove triple or more newlines (convert to double newlines)
    content = re.sub(r'\n{3,}', r'\n\n', content)
    
    return content


def process_file(file_path):
    """
    Process a single markdown file.
    
    Args:
        file_path (str): Path to the markdown file
    
    Returns:
        bool: True if file was modified, False otherwise
    """
    print(f"Processing {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        formatted_content = format_article(original_content)
        
        if original_content != formatted_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(formatted_content)
            print(f"✅ Formatted {file_path}")
            return True
        else:
            print(f"✓ No changes needed for {file_path}")
            return False
    
    except Exception as e:
        print(f"❌ Error processing {file_path}: {str(e)}")
        return False


def process_directory(directory_path):
    """
    Process all markdown files in the given directory.
    
    Args:
        directory_path (str): Path to the directory containing markdown files
    
    Returns:
        tuple: (total_files, modified_files)
    """
    md_files = glob.glob(os.path.join(directory_path, "*.md"))
    total_files = len(md_files)
    modified_files = 0
    
    print(f"Found {total_files} markdown files in {directory_path}")
    
    for file_path in md_files:
        if process_file(file_path):
            modified_files += 1
    
    return total_files, modified_files


def main():
    if len(sys.argv) < 2:
        print("Usage: python format_newsletter.py path/to/file.md")
        print("       python format_newsletter.py path/to/directory/")
        sys.exit(1)
    
    target_path = sys.argv[1]
    
    if os.path.isfile(target_path):
        if target_path.endswith('.md'):
            process_file(target_path)
        else:
            print(f"❌ {target_path} is not a markdown file")
    
    elif os.path.isdir(target_path):
        total, modified = process_directory(target_path)
        print(f"\n📊 Summary: Modified {modified} out of {total} files")
    
    else:
        print(f"❌ Path not found: {target_path}")
        sys.exit(1)


if __name__ == "__main__":
    main() 