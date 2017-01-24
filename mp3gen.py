#!/usr/bin/python
# -*- coding: utf-8 -*- #
# This would be a lot easier with a shellscript.
# Will probably just do this in bash, once I make this work.
# In this case we're doing it for educational purposes.
# Expect future revisions to be faster and more efficient.
# Started with working code, broke it to fit my needs.
# Makes me very sad, and way more work to figure out than ls *.mp3
# but at least it's not full on regex? :p

# by steakwipe with way too much help from beatsteak

#importing old soup for good luck
import os

#yt variable needed later
yt=https://youtu.be/
mp3list = '/home/steakwipe/git/ytdl-namer' #i'd like this to be a runtime option later

# let's look around here for some mp3s
def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)


# next we are attempting to process all.mp3 files in the dir
# to isolate the part of teh filename that is for YT.
# pretty much dies right away, but i basically did this
# in a python console with a single file.
# splitext, grab the first piece, then trim off the last
# 11 characters. Should result in NVEzFqKGrXY or something.
# broke as fuck. hopefully i've at least got the right idea.
# this'll need to chew thru hundreds of mp3s at a time
# and pushing the output youtube url's back in as id3 tags.

for mp3file in mp3gen():
    fn = os.path.splitext(os.path.basename('mp3file')),
    text=print([fn[0]]),
    url = text[-11::],
    print(yt+url)
