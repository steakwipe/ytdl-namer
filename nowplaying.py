#!/usr/bin/python
# -*- coding: utf-8 -*-
# the only encoding supported by my machine is utf-8
# going for the record of shittiest overcommented scripts of 2017
# by steakwipe with way too much help from beatsteak

# Python loads DBUS so we can ask it things, and SYS so we can handle unicode (i think).

import dbus
import sys

# Here we're just giving our bus a nickname. bus
bus = dbus.SessionBus()

# Here, we're telling Python that when we say 'player' we mean clementine.
# Later we'll expand this to check for different players.
player = dbus.SessionBus().get_object('org.mpris.MediaPlayer2.clementine', '/org/mpris/MediaPlayer2', 'byte_arrays=True')


# Finally we tell Python what we require of clementine. Song metadata.
metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')

# This shit works below
print("Now playing:"),
print(metadata[u'xesam:title']).encode('utf-8'),
print ("performed by"),
print(metadata[u'xesam:artist'][0]).encode('utf-8'),
print (" || "),

# print(metadata[u'xesam:albumArtist']).encode('utf-8') # broken if no tag, commented for now