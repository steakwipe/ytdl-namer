by @steakwipe with way too much help from beatsteak

Uses youtube-dl and eventually some script-fu to download MP3 files from YouTube, and process the filenames and tags to be more useful.

This script expects a file named 'list' containing a list of YT URLs. Eats anything yt-dl can, probably.

Included list is a few tracks from https://www.youtube.com/user/NoCopyrightSounds

A basic outline of what I hope to accomplish and the vague method we'll use is commented into ytdl.sh right now, hoping to get some more eyes on this.


TODO Section; not keeping a separate file for now due to the small size of the project

* expand script to support all mpris2 players, apparently not too complicated.
* instead of using sed/regex to clean up data for tags, python has done the job nicely
* primary task is to get a loop running on mp3list to trim out YT links, combine with
    variable yt (https://youtu.be/) like print(yt+url)  through mutagen, and back into
    the file in question.

    Example being this file:

            Dolls Of Pain - Cybersex-NVEzFqKGrXY.mp3
            Artist          Title     URL        ext

     Currently have working code to trim this. splitext() will remove .mp3
     Setting the track as "name" here will assist with retrieving the URL.

     From here,

        $splittext("Dolls Of Pain - Cybersex-NVEzFqKGrXY.mp3")

     will yield "Dolls Of Pain - Cybersex-NVEzFqKGrXY".
     From there,

        $name = "Dolls Of Pain - Cybersex-NVEzFqKGrXY"

     Then we just need to do:

        $url = name[11::], leaving NVEzFqKGrXY

     At this point we simply need to do

     $print(yt+url)

     to get a full YT URL.

     From there we can pass it along to mutagen. The main tag we're looking
     to set in Mutagen is TPE2. This is known as the Band/Orchestra tag,
     or more commonly "Album Artist". This is the unpopular tag that we
     will utilize for our URL, no idea how to do that yet but it doesn't look hard.
