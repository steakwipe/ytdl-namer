#!/bin/sh
#youtube-dl mp3 list ripper timesaver
#expects a file named 'list' containing a list of YT URLs. Eats anything yt-dl can, probably.
#included list is a few tracks from https://www.youtube.com/user/NoCopyrightSounds

youtube-dl -x --audio-format mp3 --metadata-from-title "%(artist)s - %(title)s" --add-metadata --batch-file=list 

## Likely will remove file tagging responsibility from youtube-dl.
## We'll pass it along to a script utilizing mid3v2 (alternative to id3v2, less broken)
## 
##

## This is where we'll do some grep-fu and such, in order to separate the filename into three pieces. By default, youtube tracks are downloaded as "ARTISTNAME - SONGTITLE - YOUTUBEURL.mp3". We simply need to separate these three, and add https://youtu.be/ to the beginning of the YOUTUBEURL. 

# The plan is to have the full youtube URL accessible from the id3 tag. This will enable some sweet functionality on those annoying /np scripts on IRC. Instead of just giving the song name, it'll output a link to the song on youtube. Currently planning to use the Album field but this is less than ideal. Pending planning.
