from enum import Enum
class player(Enum):
    MPV = 0
    VLC = 1

# class selectP(Enum):
#     mpv = 1
#     vlc = 2

p = player
apk = ["MPV", "VLC"]
def getPlayer(input):
    if input == p.MPV.name:
      print("MPV")
    elif input == p.VLC.name:
      print("VLC")
    # return apk[player.players.name]
getPlayer("MPV")

# print(getPlayer("MVP"))
# print("test")
