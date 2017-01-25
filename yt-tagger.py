#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
YouTube URL generator/tagger
by steakwipe with a ridiculous amount of help from beatsteak
#steakhouse // #ninjapirate // freenode
"""

# commenty var reminders for now

# yt="https://youtu.be/"
# name=specific filename
# URL=garbly part
# f=music directory. make this modifiable at runtime later!!!

# yt="https://youtu.be/"
# name=specific filename
# URL=garbly part
# musdir=music directory. make this modifiable at runtime later!!!

import os, re, glob

# variables. someday htese will be auto set or assignable at runtime
yt = "https://youtu.be/"
musdir = "/home/steakwipe/git/ytdl-namer"
thelist = "glob(musdir/*.mp3)"


