#!/bin/sh
#youtube-dl mp3 list ripper timesaver
#expects a file named 'list' containing a list of YT URLs. Eats anything yt-dl can.
#
youtube-dl -i -w --audio-quality 0 -r 300K --extract-audio --audio-format mp3 --batch-file=list --add-metadata
