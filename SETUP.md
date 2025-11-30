# Setup Guide for Chirpy Theme

## Installation Steps

### 1. Install Ruby Dependencies

```bash
bundle install
```

If you don't have Bundler installed:
```bash
gem install bundler
```

### 2. Run the Site Locally

```bash
bundle exec jekyll serve
```

Or with live reload:
```bash
bundle exec jekyll serve --livereload
```

The site will be available at `http://localhost:4000`

### 3. Build for Production

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

## Troubleshooting

### Issue: Bundle install fails

**Solution:** Make sure you have Ruby 3.0+ installed:
```bash
ruby --version
```

### Issue: Jekyll command not found

**Solution:** Install Jekyll:
```bash
gem install jekyll
```

### Issue: Permission errors on macOS/Linux

**Solution:** Use user-level gem installation:
```bash
bundle install --path vendor/bundle
```

## GitHub Pages Deployment

### Option 1: GitHub Actions (Recommended)

The site will automatically build and deploy when you push to the main branch.

### Option 2: Manual Build

1. Build the site:
   ```bash
   JEKYLL_ENV=production bundle exec jekyll build
   ```

2. The built site will be in `_site/` directory

3. Push to your GitHub Pages repository

## Customization

### Adding Blog Posts

Create a new file in `_posts/` with format: `YYYY-MM-DD-title.md`

Example:
```markdown
---
title: My New Post
date: 2024-12-01 10:00:00 -0500
categories: [Category1, Category2]
tags: [tag1, tag2]
---

Your content here...
```

### Modifying Navigation

Edit files in `_tabs/` folder. Each file becomes a navigation tab.

### Changing Site Configuration

Edit `_config.yml` to update:
- Site title and description
- Social media links
- Analytics
- Comments system
- Theme settings

### Adding Images

Place images in `images/` or `assets/img/` folder and reference them:
```markdown
![Alt text](/images/your-image.png)
```

## Resources

- [Chirpy Documentation](https://chirpy.cotes.page/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
