# Quick Reference Guide

## 🚀 Common Commands

### Start Development Server
```bash
bundle exec jekyll serve
```

### Start with Live Reload
```bash
bundle exec jekyll serve --livereload
```

### Build for Production
```bash
JEKYLL_ENV=production bundle exec jekyll build
```

### Update Dependencies
```bash
bundle update
```

## 📝 Creating Content

### New Blog Post Template
Create: `_posts/2024-12-01-my-post-title.md`

```markdown
---
title: My Post Title
date: 2024-12-01 10:00:00 -0500
categories: [Category1, Category2]
tags: [tag1, tag2, tag3]
pin: false
---

Your content here...

## Heading 2

### Heading 3

**Bold text** and *italic text*

- Bullet point 1
- Bullet point 2

1. Numbered item 1
2. Numbered item 2

![Image description](/images/image.png)

[Link text](https://example.com)
```

### New Navigation Tab
Create: `_tabs/my-page.md`

```markdown
---
icon: fas fa-icon-name
order: 6
---

# Page Title

Your content here...
```

## 🎨 Front Matter Options

### For Blog Posts
```yaml
---
title: Post Title              # Required
date: 2024-12-01 10:00:00 -0500  # Required
categories: [Cat1, Cat2]       # Optional
tags: [tag1, tag2]             # Optional
pin: true                      # Pin to top (optional)
image:                         # Post image (optional)
  path: /images/post-image.png
  alt: Image description
---
```

### For Pages
```yaml
---
layout: page                   # Optional (default)
title: Page Title              # Optional
icon: fas fa-icon-name         # For tabs
order: 1                       # Tab order
---
```

## 📁 File Locations

| Content Type | Location | Example |
|--------------|----------|---------|
| Blog Posts | `_posts/` | `2024-12-01-title.md` |
| Navigation Tabs | `_tabs/` | `about.md` |
| Images | `images/` or `assets/img/` | `profile.png` |
| Configuration | Root | `_config.yml` |
| Drafts | `_drafts/` | `draft-post.md` |

## 🔧 Configuration Quick Edits

### Change Site Title
Edit `_config.yml`:
```yaml
title: Your New Title
```

### Change Tagline
```yaml
tagline: Your new tagline
```

### Update Social Links
```yaml
social:
  name: Your Name
  email: your@email.com
  links:
    - https://twitter.com/username
    - https://github.com/username
```

### Enable Analytics
```yaml
analytics:
  google:
    id: G-XXXXXXXXXX
```

### Enable Comments
```yaml
comments:
  provider: giscus  # or disqus, utterances
  giscus:
    repo: username/repo
    repo_id: your-repo-id
    category: Announcements
    category_id: your-category-id
```

## 🎯 Font Awesome Icons

Common icons for tabs:
- `fas fa-info-circle` - Info (About)
- `fas fa-archive` - Archive
- `fas fa-stream` - Categories
- `fas fa-tags` - Tags
- `fas fa-file-alt` - Document (CV)
- `fas fa-home` - Home
- `fas fa-user` - User
- `fas fa-briefcase` - Work
- `fas fa-graduation-cap` - Education
- `fas fa-code` - Code/Projects

Find more at: [Font Awesome Icons](https://fontawesome.com/icons)

## 🖼️ Image Syntax

### Basic Image
```markdown
![Alt text](/images/image.png)
```

### Image with Caption
```markdown
![Alt text](/images/image.png)
_Image caption here_
```

### Centered Image
```markdown
{: .text-center}
![Alt text](/images/image.png)
```

## 📊 Code Blocks

### Inline Code
```markdown
Use `inline code` like this.
```

### Code Block with Language
````markdown
```python
def hello():
    print("Hello, World!")
```
````

### Code Block with Line Numbers
````markdown
```python
# This will show line numbers automatically
def hello():
    print("Hello, World!")
```
````

## 🔗 Links

### External Link
```markdown
[Link text](https://example.com)
```

### Internal Link
```markdown
[About page](/about/)
[Blog post](/posts/post-title/)
```

### Link with Title
```markdown
[Link text](https://example.com "Hover title")
```

## 📋 Lists

### Unordered List
```markdown
- Item 1
- Item 2
  - Nested item
  - Another nested item
- Item 3
```

### Ordered List
```markdown
1. First item
2. Second item
3. Third item
```

### Task List
```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

## 💡 Tips

### Pin Important Posts
Add `pin: true` to front matter to pin posts to the top of the home page.

### Use Categories Wisely
Use 1-2 broad categories per post (e.g., "AI", "Personal", "Tutorial").

### Use Tags Liberally
Use multiple specific tags per post (e.g., "python", "machine-learning", "tutorial").

### Draft Posts
Create posts in `_drafts/` folder (no date needed) to work on them before publishing.

### Preview Drafts
```bash
bundle exec jekyll serve --drafts
```

## 🆘 Troubleshooting

### Site not loading?
- Check if Jekyll server is running
- Check for errors in terminal
- Try `bundle exec jekyll clean` then rebuild

### Changes not showing?
- Hard refresh browser (Ctrl+F5 or Cmd+Shift+R)
- Check if file is saved
- Restart Jekyll server

### Build errors?
- Check YAML front matter syntax
- Check for special characters in filenames
- Run `bundle exec jekyll build --verbose`

## 📚 Resources

- [Chirpy Docs](https://chirpy.cotes.page/)
- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Font Awesome](https://fontawesome.com/icons)
