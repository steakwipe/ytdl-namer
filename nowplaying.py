#!/usr/bin/python
# encoding: utf-8
# the only encoding supported by my machine is utf-8
# going for the record of shittiest overcommented script of 2017
# by steakwipe

# Python loads DBUS so we can ask it things.
import dbus,sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Here we're just giving our bus a nickname. "bus"
bus = dbus.SessionBus()
# Here, we're telling Python that when we say "player" we mean clementine.
player = dbus.SessionBus().get_object('org.mpris.MediaPlayer2.clementine', '/org/mpris/MediaPlayer2')

# Finally we tell Python what we require of clementine. Song metadata.
metadata = player.Get('org.mpris.MediaPlayer2.Player', 'Metadata', dbus_interface='org.freedesktop.DBus.Properties')

# This is just the unnatural fuckery I used to cut the Artist and Title
# out of the metadata. The commas at the end of the line tell Python
# not to start a new line when running. This causes the entire output to go along one line, ready for spamming into IRC
print("Now playing: "),
print(metadata[u'xesam:title']).encode('utf-8'),
print ("performed by"),
print(metadata[u'xesam:albumArtist'][0]).encode('utf-8')



####
# todo, cause fuck it why not #
			   ####
# should probably eventually wrap this up for hexchat consumption
# current scripts available online do not seem to work because
# clementine does not appear to support MPRIS1.0 any longer, unable to verify via irc though.
# wtf
# reach out to folks who are familiar with hexchat scripts to find out
# the bare minimum i'd need to execute from within hexchat. 
# 
# attempt hexchat.command("me switchover- requires actually being loaded into hexchat i'm sure.

