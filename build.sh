#!/bin/bash

# Echo commands for debugging
set -x

# Create output directory
mkdir -p output

# Print current directory
pwd

# Add current directory to Python path
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Install dependencies using pip if uv is not available
if command -v uv &> /dev/null; then
    uv pip install -r requirements.txt
else
    pip install -r requirements.txt
fi

# Show Python version
python --version

# Show current directory contents
ls -la

# Build the site
echo "Building site using Pelican..."
pelican content -o output -s publishconf.py

# Create a Netlify _redirects file in the output directory
echo "/* /index.html 200" > output/_redirects

# List output directory contents
ls -la output 