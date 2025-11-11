# Local Testing Guide

## Local Development Server

For the best testing experience, use the local development server:

```bash
python local-server.py
```

This will:
- Start a local HTTP server on `http://localhost:8000/`
- Open your browser automatically
- Enable full functionality including localStorage
- Provide the most accurate testing environment

## Testing Features

### Theme System
- Navigate to `theme.html`
- Change colors and click "Apply Theme"
- Navigate to other pages to verify theme persistence
- Refresh pages to test theme storage

### Navigation
- Test navigation between all pages
- Verify navbar works correctly
- Check responsive design

### Clock Feature
- Test the digital clock functionality
- Use the size slider to adjust clock size
- Verify real-time updates

## Quick Testing

1. **Start server**: `python local-server.py`
2. **Test navigation**: Click through all pages
3. **Test themes**: Use theme page to customize colors
4. **Test clock**: Verify clock functionality and sizing

## Deployment

When deployed to GitHub Pages or any web server, all features will work without any additional configuration.