import os
import re

# Read the navbar template
with open('components/navbar.html', 'r', encoding='utf-8') as f:
    navbar_content = f.read()

# List of HTML files to update
html_files = [
    'index.html',
    'clock.html', 
    'theme.html'
]

# Process each HTML file
for file in html_files:
    file_path = file
    
    # Read the current content
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the navbar placeholder with actual navbar content
    # Look for the navbar-container div and replace its content
    content = re.sub(
        r'<div id="navbar-container"></div>',
        f'<div id="navbar-container">{navbar_content}</div>',
        content
    )
    
    # Write the updated content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'✅ Updated navbar in {file}')

print('🎉 Navbar build completed!')