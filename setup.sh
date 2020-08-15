#!/bin/bash

echo 'Sdl'
sudo apt-get install libsdl-dev libsdl-image1.2-dev \
libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev

echo 'ffmpeg'
sudo apt-get install ffmpeg

echo 'python'
pip3 install -r requirements.txt