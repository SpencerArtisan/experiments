class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

rainbows = Song(["And now","I can see", "there's a way out"])
rainbows.sing_me_a_song()
