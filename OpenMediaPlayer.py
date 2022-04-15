
def mediaPlayer():
    setup = {}
    MPlayer = int(input("Buka dengan :\n[1] MVP\n[2] VLC\n: "))
    if MPlayer == "MVP":
        setup['player'] = "mvp"
    else :
        setup['player'] = "vlc'
    
