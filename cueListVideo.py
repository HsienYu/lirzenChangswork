from gpiozero import LEDBoard
from omxplayer import OMXPlayer
from time import sleep
from pathlib import Path


outlets = LEDBoard(a1=2, a2=15, a3=18, a4=23, a5=24, a6=25, a7=8,
                   a8=7, a9=3, a10=4, a11=27, a12=14, a13=17, a14=22, a15=10, a16=9)

VIDEO_PATH = Path("/media/USB/main.mp4")

sleep(5)

player = OMXPlayer(VIDEO_PATH, args=[
                   '--loop', '--no-osd', '--blank'])


def reset_gpio():
    for o in outlets:
        o.off()


class Cue():

    def __init__(self, p):
        self.pos = p

    def __call__(self, w, i, o, t):
        self.wait = w
        self.inTime = i
        self.outTime = o
        self.target = t
        while self.pos > self.wait:
            if self.pos >= self.inTime and self.pos <= self.outTime:
                outlets[self.target].on()
                print(f'{self.target} is on')
            else:
                outlets[self.target].off()
                print(f'{self.target} is off')
            break


class sp_Cue():

    def __init__(self, p):
        self.pos = p

    def __call__(self, w, t):
        self.wait = w
        self.target = t
        while self.pos > self.wait:
            outlets[self.target].on()
            print(f'{self.target} is on')
            break


reset_gpio()

outlets[9].on()

while (1):
    position = player.position()
    print(position)
    cue = Cue(position)
    sp_cue = sp_Cue(position)
    # pre cue time, inTime, outTime, channal
    cue(1, 1.4, 18, 6)  # 7
    cue(1, 1.4, 18, 7)  # 8
    cue(1, 1.4, 18, 8)  # 9
    cue(18, 10000, 10000, 9)  # 10  # main light off 18sec
    cue(18, 19, 1565, 10)  # 11
    cue(82, 83, 135, 0)  # 1
    cue(138, 138.6, 163.1, 6)  # 7
    cue(170, 171.4, 206.4, 6)  # 7
    cue(170, 171.4, 206.4, 7)  # 8
    cue(170, 171.4, 206.4, 8)  # 9
    cue(436, 437, 485, 7)  # 8
    cue(561, 562.7, 583.5, 0)  # 1
    cue(633, 634.7, 724.6, 6)  # 7
    cue(633, 634.7, 724.6, 7)  # 8
    cue(633, 634.7, 724.6, 8)  # 9
    cue(845, 847, 915.2, 1)  # 2
    cue(869, 870, 884, 7)  # 8
    cue(843, 884.2, 895.8, 6)  # 7
    cue(896, 897, 908.5, 7)  # 8
    cue(909, 909.7, 915.2, 8)  # 9
    cue(918, 918.5, 984, 4)  # 5
    cue(966, 966.2, 1042.7, 7)  # 8
    cue(1125, 1126, 1160, 2)  # 3
    cue(1260, 1261, 1304.8, 3)  # 4
    cue(1329, 1329.6, 1362, 6)  # 7
    cue(1372, 1372.5, 1435, 7)  # 8
    cue(1425, 1425.6, 1442.2, 5)  # 6
    sp_cue(1564, 9)  # 10  # main light on 1565sec
    cue(1592, 1593, 1740, 6)  # 7

    # cue(1, 2, 5, 0)
    # cue(1, 5, 10, 1)
    # cue(1, 10, 15, 2)
    # cue(1, 15, 20, 3)
    # cue(1, 20, 25, 4)
    # cue(1, 25, 30, 5)
    # cue(1, 30, 35, 6)
    # cue(1, 35, 40, 7)
    # cue(1, 45, 50, 8)
    # cue(1, 50, 55, 9)
    # cue(1, 60, 65, 10)
