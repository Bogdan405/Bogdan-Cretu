# Navbar Build Process

## Problem
- CORS restrictions prevent loading `components/navbar.html` when opening HTML files directly
- Need single-source navbar for easy maintenance

## Solution
- **Single Source**: Edit `components/navbar.html`
- **Build Process**: Run build script to embed navbar into all HTML files

## How to Use

1. Run: `python build-navbar.py`
2. All HTML files will be updated with the latest navbar

## Files Updated
- `index.html`
- `clock.html`
- `theme.html`

## Benefits
- ✅ No CORS issues when opening files directly
- ✅ Single source of truth for navbar
- ✅ Fast and reliable
- ✅ Works in all browsers and environments