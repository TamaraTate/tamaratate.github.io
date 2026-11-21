# Tamara Tate’s website

A static academic site prepared for GitHub Pages. Open `index.html` in a web browser to preview the site offline. The home, resources, and archive pages all work without a build service.

## Update the site

Edit the appropriate HTML fragment in `content/`, then run `python3 scripts/build.py` from the repository root. For example, publications are in `content/selected-publications.html`, projects in `content/funded-projects.html`, and talks in `content/speaking.html`. Commit both the fragment and the rebuilt pages. The published pages use the generated HTML at the repository root.

To update the CV, replace `uploads/2/0/8/8/20880284/tate_cv.pdf` in place. The previous CV and slide PDFs retain their existing Weebly-era paths.

## Publish a preview

Create the repository `TamaraTate/tamaratate.github.io`, add these files at the repository root, then choose the main branch and root folder in **Settings → Pages**. The dotfile `.nojekyll` tells GitHub Pages to serve the static files as supplied. See [GitHub’s Pages setup guide](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

Review the GitHub Pages URL before pointing tptate.com at it. Confirm the older pages from the Weebly sitemap, hosted downloads, external slides links and mobile layout. The separate historical ASEE PDF URL returned 404 from Weebly. The conference item’s current paper link is retained.

The domain’s DNS can stay with the current provider. When the preview is approved, configure the custom domain and HTTPS using [GitHub’s domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).
