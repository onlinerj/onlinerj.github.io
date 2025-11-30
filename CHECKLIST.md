# Post-Migration Checklist

Use this checklist to ensure your Chirpy theme is fully set up and customized.

## ✅ Initial Setup

- [ ] Run `bundle install` (or `./setup.sh` on Mac/Linux, `setup.bat` on Windows)
- [ ] Run `bundle exec jekyll serve` to test locally
- [ ] Visit `http://localhost:4000` and verify the site loads
- [ ] Check all navigation tabs work (About, Archives, Categories, Tags, CV)

## ✅ Content Review

- [ ] Review `_tabs/about.md` - update with any missing information
- [ ] Review `_tabs/cv.md` - add detailed work experience and education
- [ ] Review blog posts in `_posts/` - edit or add more content
- [ ] Check that profile image displays correctly

## ✅ Configuration

- [ ] Update `_config.yml` with any additional settings
- [ ] Add Google Analytics ID (if you want analytics)
- [ ] Configure comments system (Disqus, Utterances, or Giscus)
- [ ] Add site verification codes (Google, Bing, etc.)
- [ ] Review social media links are correct

## ✅ Customization

- [ ] Choose theme mode (light/dark/auto) in `_config.yml`
- [ ] Add favicon images (optional)
- [ ] Customize colors (optional, requires editing `_sass/`)
- [ ] Add more navigation tabs if needed

## ✅ Content Creation

- [ ] Write and publish your first real blog post
- [ ] Add categories and tags to organize content
- [ ] Add images to `images/` or `assets/img/` folder
- [ ] Create drafts in `_drafts/` folder (optional)

## ✅ SEO & Performance

- [ ] Update meta descriptions in `_config.yml`
- [ ] Add social preview image
- [ ] Test site speed
- [ ] Verify mobile responsiveness

## ✅ Deployment

- [ ] Commit all changes to git
- [ ] Push to GitHub
- [ ] Verify GitHub Actions workflow runs successfully
- [ ] Check deployed site at `https://onlinerj.github.io`
- [ ] Test all links and pages on live site

## ✅ Cleanup (Optional)

After confirming everything works:

- [ ] Delete old `_pages/` folder
- [ ] Delete old `_includes/` folder
- [ ] Delete old `_layouts/` folder
- [ ] Delete old `_sass/` folder (not the new one!)
- [ ] Delete old `assets/js/plugins/` folder
- [ ] Delete old `assets/css/` folder
- [ ] Keep `images/` folder
- [ ] Keep `_data/cv.json` if you want to reference it

## ✅ Advanced Features (Optional)

- [ ] Enable PWA (Progressive Web App) features
- [ ] Set up RSS feed customization
- [ ] Add math equation support (KaTeX)
- [ ] Configure CDN for media resources
- [ ] Set up custom domain (if applicable)

## 📝 Notes

Write any issues or customizations you want to remember:

```
[Your notes here]
```

## 🎯 Priority Tasks

Mark your top 3 priorities:

1. [ ] _______________________________
2. [ ] _______________________________
3. [ ] _______________________________

---

**Last Updated:** [Add date when you complete this checklist]
