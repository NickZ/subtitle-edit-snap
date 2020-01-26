# Subtitle Edit snap packaging

This package makes it very easy to run subtitle-edit on Linux.

[Download here](https://github.com/NickZ/subtitle-edit-snap/releases)

To install, run:

`sudo snap install --dangerous subtitle-edit*.snap`

After installation, please run these commands or it will not work:

```
sudo snap connect subtitle-edit:alsa :alsa
sudo snap connect subtitle-edit:removable-media :removable-media
sudo snap connect subtitle-edit:mount-observe :mount-observe
```

The build of Subtitle Edit that I'm using in this comes from this branch: [NickZ/snap-debug-build](https://github.com/NickZ/subtitleedit/tree/snap-debug-build)

