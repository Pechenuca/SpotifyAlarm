Установка
====================

Требования:
    sdl2, ffmpeg, python 3.7 и аудио-девайс

    .. image:: imgs/know.gif
        :width: 400
        :alt: Alternative text

*********
windows
*********

SDL
^^^^^^^^^

sdl установиться вместе с pygame, но если что-то пошло не по плану
ссылка: http://www.libsdl.org/download-2.0.php


ffmpeg
^^^^^^^^^

ссылка: http://ffmpeg.zeranoe.com/builds/
распакуйте архив например в C:\ffmpeg

и добавте в PATH

    .. image:: imgs/pathEx.png
        :width: 400
        :alt: Alternative text


pip
^^^^^^^^^

.. code-block:: shell

    pip3 install -r requirements.txt

*********
linux
*********

SDL
^^^^^^^^^

.. code-block:: shell


    sudo apt-get install libsdl-dev libsdl-image1.2-dev \
    libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev libportmidi-dev \
    libavformat-dev libswscale-dev libjpeg-dev libfreetype6-dev


ffmpeg
^^^^^^^^^

.. code-block:: shell

    sudo apt-get install ffmpeg


pip
^^^^^^^^^

.. code-block:: shell

    pip3 install -r requirements.txt


или вы можете просто запустить sh скрипт из корня проекта

.. code-block:: shell

    ./setup.sh