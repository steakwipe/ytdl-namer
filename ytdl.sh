#!/bin/sh
#youtube-dl mp3 list ripper timesaver
#expects a file named 'list' containing a list of YT URLs. Eats anything yt-dl can, probably.
#included list is a few tracks from https://www.youtube.com/user/NoCopyrightSounds

youtube-dl -x --audio-format mp3 --metadata-from-title "%(artist)s - %(title)s" --add-metadata --batch-file=list 

