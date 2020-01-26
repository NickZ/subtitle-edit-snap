#!/bin/bash

sudo snap remove --purge subtitle-edit
sudo snap install --dangerous --devmode subtitle-edit_*_amd64.snap
sudo snap connect subtitle-edit:alsa :alsa
sudo snap connect subtitle-edit:removable-media :removable-media
