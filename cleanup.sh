#!/bin/bash

# Script to clean up temporary files and .DS_Store files

# Echo commands for debugging
set -x

# Find and remove all .DS_Store files
echo "Removing .DS_Store files..."
find . -name ".DS_Store" -type f -delete

# Remove any Python cache files
echo "Removing Python cache files..."
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -type f -delete
find . -name "*.pyo" -type f -delete
find . -name "*.pyd" -type f -delete

# Clean output directory
echo "Cleaning output directory..."
rm -rf output

echo "Cleanup complete!" 