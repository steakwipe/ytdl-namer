#!/usr/bin/python
# -*- coding: utf-8 -*- #
# This would be a lot easier with a shellscript.
# In this case we're doing it for educational purposes.
# Expect future revisions to be faster and more efficient.
# Confirmed working code and way more work to figure out than ls *.mp3

import os


def mp3find():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)


for mp3file in mp3find():
    print mp3file

# So now we're left with mp3file. I really want to give
# it a $ or something because I am not used to these less
# than obvious