# claudiochato.github.io

Código do linktree do Cláudio, o Chato no Instagram. Built with Hugo and deployed to GitHub Pages at https://claudiochato.github.io/.

- **Edit the links:** `data/links.yaml`
- **Thumbnails:** in `data/links.yaml`, `url` is where the entry links to and `instagram` is your post that supplies its thumbnail. Set `instagram`, then run `python3 scripts/miniatura.py`. It saves any missing thumbnails to `assets/miniaturas/`, so commit those too. If Instagram refuses the download, save the image yourself and run `python3 scripts/miniatura.py URL --ficheiro image.jpg`.
- **Mascot:** put `mascote.png` at `static/img/mascote.png`. Until then the avatar shows a "C".
- **Preview:** `hugo server`
- **Deploy:** push to `main`.

## License

The code is under the MIT License (see `LICENSE`). That license does not cover the name "Cláudio, o Chato", the mascot, the thumbnails or the other brand and post images, which are all rights reserved.
