from pygame import mixer
mixer.init()
mixer.music.load('test.mp3')
mixer.music.play()
input('Are you listening to this epic sound ?')