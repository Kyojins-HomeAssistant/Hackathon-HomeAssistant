import os

os.environ["PATH"] = os.path.dirname(__file__) + os.pathsep + os.environ["PATH"]

import mpv

player = mpv.MPV(ytdl=True, video=False)

player.play('https://open.spotify.com/track/5VC29kHMkzcaorzPKUqJbl?si=de8f91dd5b2b43b5')
player.wait_for_playback()