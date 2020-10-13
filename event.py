#! /usr/bin/python

# Copyright (C) 2012 Maxwell J. Koo <mjkoo90@gmail.com>
#
# Based on code originally by John Reese, LeetCode.net
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#====This file has been modified to work with piandora.....
import contextlib
import hashlib
import os
import sys
import subprocess
import time
from urllib2 import urlopen, URLError

title = "empty title"
song_duration = " | -"
artist_album = "empty artist"

def handle_event(type, **kwargs):
    global playtime
    """
    Read event parameters from stdin and handle events appropriately.
    """
    # Error from pianobar, disregard
    if kwargs.get("pRet") != "1":
        return
    # Handle specific events
    if type == "songstart":
        title = kwargs.get("title")
        cover_url = kwargs.get("coverArt")
        artist_album = " | by %s on %s" % (kwargs.get("artist"), kwargs.get("album"))
        song_duration = " | %s"% (kwargs.get("songDuration"))
        song_played = kwargs.get("songPlayed")
        rating = kwargs.get("rating")
#        station = kwargs.get("stationNum")
#        print("==type " + type)
        print("===song -" + title)
        print("===atist -  " + artist_album)
        print("===duration - " + song_duration)
#        print("===songplayed - " + song_played)
#        print("===rating - " + rating)
#        print("===param - " + param)
#        print("===value - " + value)
 
        config_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
        filename = os.path.join(config_dir, "covers", hashlib.sha1(cover_url).hexdigest())
        cover = fetch_cover(cover_url, filename)

        playtime = ' | rst'
        file1 = open("data.txt","w")
        Line = [title, artist_album, playtime, song_duration]
        file1.writelines(Line)
        file1.close()
        time.sleep(4)
        playtime = ' | play'
        file1 = open("data.txt","w")
        Line = [title, artist_album, playtime, song_duration]
        file1.writelines(Line)
        file1.close()
        

def fetch_cover(url, filename):
    global title
    """
    Fetches album art from the URL specified by pianobar, and saves to disk.
    """

    # If the "covers" directory does not exist under the pianobar config
    # directory, create it
    if not os.path.isdir(os.path.dirname(filename)):
        os.mkdir(os.path.dirname(filename))

    if not os.path.exists(filename):
        try:
            with contextlib.closing(urlopen(url)) as inf, open(filename, "wb") as outf:
                outf.write(inf.read())
        except URLError:
            return ""

    print("===Saved cover to home folder ==")
    subprocess.call("mv covers/* cover.jpg", shell=True)
    return "file://%s" % filename

def main(argv=None):
    global title
    global param
    global value

    if argv is None:
        argv = sys.argv

    # Read event type from command arguments
    if len(sys.argv) < 2:
        print "error reading event type from command arguments"

    type = sys.argv[1]
#    print("==type " + type)
    # Read parameters from input
    params = {}
    for s in sys.stdin.readlines():
        param, value = s.split("=", 1)
        params[param.strip()] = value.strip()
#    print("==params - " + s)
#    print("==value " + value)
    # Call the event handler
    handle_event(type, **params)


    return 0
if __name__ == "__main__":
    #sys.exit(main())
    main()
