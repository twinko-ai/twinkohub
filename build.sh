#!/bin/bash

# Echo commands for debugging
set -x

# Install dependencies
pip install -r requirements.txt

# Show Python version
python --version

# Show current directory contents
ls -la

# Show Python path
python -c "import sys; print(sys.path)"

# Build the site directly with pelican
pelican content -o output -s publishconf.py

# Show output directory contents
ls -la output 