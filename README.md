# Tri Nguyen portfolio

Plain HTML/CSS/JS. No framework, no build step needed to host it.

## Publish on GitHub Pages
1. Create a repo named `nhantri132.github.io` (your user site, the URL becomes https://nhantri132.github.io/).
   Or use any repo name; then set `BASE = "/<repo>/"` in build.py (only affects the 404 page) and run `python3 build.py`.
2. Upload everything in this folder to the repo root (or `git push`).
3. Repo Settings > Pages > Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
4. Wait a minute, then open the URL.

## Edit content
- Text, projects, roles, videos: edit the lists at the top of `build.py`, then run `python3 build.py`. Commit the regenerated .html files.
- Email link: set `EMAIL` in build.py (empty hides it).
- Portrait: save a photo as `assets/tri.jpg` (about 480x600). The About page hides the photo slot until it exists.
- Colors and fonts: variables at the top of `assets/style.css`.
