# Migration to Chirpy Theme

## Completed Steps

1. ✅ Installed Chirpy theme via Gemfile
2. ✅ Created new `_config.yml` with your personal information
3. ✅ Migrated About page content to `_tabs/about.md`
4. ✅ Created CV page at `_tabs/cv.md`
5. ✅ Set up Chirpy directory structure (_tabs, _posts)
6. ✅ Created sample welcome post
7. ✅ Configured social links (GitHub, Twitter, LinkedIn, Email)

## Your Personal Info Configured

- Name: Rajat Jaiswal
- Email: onlinerj@live.com
- Location: New York City
- GitHub: onlinerj
- Twitter: rajatjw
- LinkedIn: rajatjw
- Avatar: /images/profile.png

## Next Steps

1. **Install dependencies**:
   ```bash
   bundle install
   ```

2. **Run the site locally**:
   ```bash
   bundle exec jekyll serve
   ```

3. **Add more content**:
   - Create blog posts in `_posts/` folder
   - Format: `YYYY-MM-DD-title.md`
   - Use front matter with title, date, categories, tags

4. **Customize further**:
   - Update `_tabs/cv.md` with your actual CV details
   - Add more tabs if needed in `_tabs/` folder
   - Customize theme colors in `_sass/` (if needed)

## Old Files Preserved

Your old content is still in these folders:
- `_pages/` - Old page files
- `_data/cv.json` - Your CV data
- `assets/` - Old theme assets
- `_includes/`, `_layouts/`, `_sass/` - Old theme files

You can delete these once you've migrated any content you need.

## Chirpy Theme Structure

- `_tabs/` - Main navigation tabs (About, Archives, Categories, Tags, CV)
- `_posts/` - Blog posts (format: YYYY-MM-DD-title.md)
- `_config.yml` - Site configuration
- `images/` - Your images (profile.png is already configured)

## Resources

- [Chirpy Documentation](https://chirpy.cotes.page/)
- [Chirpy GitHub](https://github.com/cotes2020/jekyll-theme-chirpy)
- [Writing Posts Guide](https://chirpy.cotes.page/posts/write-a-new-post/)
