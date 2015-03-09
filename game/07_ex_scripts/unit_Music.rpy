init -999 python:


    def MusicStart(name):
        music_volume=1.0
#        music_name=name
        if name=="Supergirl":
            name="music/Reamonn-Supergirl.mp3"
            music_volume=0.3

        renpy.music.stop(fadeout=2.0)
        renpy.music.play(name, fadein=1, fadeout=1)
        renpy.music.set_volume(music_volume) 
        return

    def MusicStop():
        renpy.music.stop(fadeout=2.0)
        renpy.music.set_volume(1.0,2.0) 
        return

    def MusicVolumeReset():
        renpy.music.set_volume(1.0) 
        return
