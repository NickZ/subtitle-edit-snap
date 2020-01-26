# Subtitle Edit snap packaging

This package makes it very easy to run subtitle-edit on Linux.

To install, run:

`sudo snap install --dangerous --devmode subtitle-edit*.snap`

After installation, please run these commands or it will not work:

```
sudo snap connect subtitle-edit:alsa :alsa
sudo snap connect subtitle-edit:removable-media :removable-media
```