# Theme Migration: Academic Pages → Chirpy

## Key Differences

### Structure Changes

| Old (Academic Pages) | New (Chirpy) | Notes |
|---------------------|--------------|-------|
| `_pages/` | `_tabs/` | Main navigation pages |
| `_pages/about.md` | `_tabs/about.md` | About page |
| `_pages/cv.md` | `_tabs/cv.md` | CV/Resume page |
| `_publications/` | `_posts/` | Publications as blog posts |
| `assets/` | `assets/` | Keep your images |
| `_config.yml` | `_config.yml` | Completely rewritten |

### Configuration Changes

**Old theme used:**
- `author:` section with detailed profile
- `site_theme:` for theme selection
- Custom collections for publications

**New theme uses:**
- `social:` section for profile
- Built-in theme with customization options
- Standard `_posts/` for all content

### Navigation

**Old:** Custom navigation via `_data/navigation.yml`

**New:** Automatic navigation from `_tabs/` folder with `order:` front matter

### Content Migration

✅ **Migrated:**
- About page content → `_tabs/about.md`
- CV information → `_tabs/cv.md`
- Personal info → `_config.yml`
- Profile image → Already at `/images/profile.png`

📝 **Converted to Blog Posts:**
- Work experience → `_posts/2024-11-15-my-journey-in-ai.md`
- Projects → `_posts/2024-12-01-my-projects.md`
- Extracurricular → `_posts/2024-10-20-adventures-and-challenges.md`

🗂️ **Preserved (not migrated yet):**
- Old `_pages/` folder
- Old `_data/cv.json`
- Old theme files in `_includes/`, `_layouts/`, `_sass/`
- Old `assets/` folder

## What You Get with Chirpy

### Features

✨ **Modern Design:**
- Clean, minimalist interface
- Dark/light mode toggle
- Responsive mobile design
- Fast loading times

📱 **Better Navigation:**
- Sidebar navigation
- Categories and tags
- Archive page
- Search functionality

🎨 **Enhanced Content:**
- Syntax highlighting
- Table of contents
- Image captions
- Math equations support (KaTeX)

📊 **Built-in Features:**
- SEO optimization
- RSS feed
- Sitemap
- PWA support
- Analytics integration

### Customization Options

You can customize:
- Color schemes (light/dark)
- Social media links
- Avatar/profile image
- Site description
- Analytics (Google, GoatCounter, etc.)
- Comments (Disqus, Utterances, Giscus)

## Next Steps

1. **Test locally:**
   ```bash
   bundle install
   bundle exec jekyll serve
   ```

2. **Review migrated content:**
   - Check `_tabs/about.md`
   - Check `_tabs/cv.md`
   - Review blog posts in `_posts/`

3. **Customize further:**
   - Update `_config.yml` with analytics IDs
   - Add more blog posts
   - Customize colors (if needed)

4. **Clean up old files** (after confirming everything works):
   - Delete old `_pages/` folder
   - Delete old `_includes/`, `_layouts/`, `_sass/` folders
   - Delete old `assets/js/`, `assets/css/` folders
   - Keep `images/` folder

5. **Deploy:**
   - Push to GitHub
   - GitHub Actions will automatically build and deploy

## Resources

- [Chirpy Demo](https://chirpy.cotes.page/)
- [Writing Posts Guide](https://chirpy.cotes.page/posts/write-a-new-post/)
- [Customization Guide](https://chirpy.cotes.page/posts/customize-the-favicon/)
