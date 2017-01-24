#!/usr/bin/python
# -*- coding: utf-8 -*-
# YouTube URL generator/tagger
# by steakwipe with a ridiculous amount of help from beatsteak
# ##steakhouse // #ninjapirate // freenode
# commenty var reminders for now

# yt="https://youtu.be/"
# name=specific filename
# URL=garbly part
# musdir=music directory. make this modifiable at runtime later!!!

import os, re, glob

# variables. someday htese will be auto set or assignable at runtime
yt = "https://youtu.be/"
musdir = "/home/steakwipe/git/ytdl-namer"
thelist = "glob(musdir/*.mp3)"


def mp3gen():
    for root, dirs, files in os.walk('[musdir]'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)


for mp3file in mp3gen():
    print mp3file