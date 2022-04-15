#import json

#buka file JSON
#file_json = open("config.json")

#mengembalikan JSON objek sebagai dictionary
#data = json.load(file_json)

#for i in data['emp_details']:
    #print(i)

def firstSetup():
    with open('./config.json','w',encoding='utf-8') as config:
            setup = {}
            print("First time setup")
            if int(input("Preferred media player :\n[1] MPV\n[2] VLC\nInput : ")) == 1 :
                setup['player'] = "mpv"
            else :
                setup['player'] = "vlc"
            setup['termux'] = input("Are you using Termux ? [y/n] : ") in ('Y','y')
            setup['anilist'] = input("Login with anilist ? [y/n] : ") in ('y','Y')
            if setup['anilist']:
                setup['token'] = anilist.login()
                setup['auto'] = input("Auto update anilist after watching anime ? [y/n] : ") in ('y','Y')
                setup['username'] = eval(anilist.getUserId(setup['token']).content)['data']['Viewer']['name']
            config.write(str(setup))
            return setup
def getconfig():
        with open('./config.json','r',encoding='utf-8') as config:
            return config.read()
    # try:
    #     with open('./config.json','r',encoding='utf-8') as config:
    #         return eval(config.read())
    # except:
    #     with open('./config.json','w',encoding='utf-8') as config:
    #         setup = {}
    #         print("First time setup")
    #         if int(input("Preferred media player :\n[1] MPV\n[2] VLC\nInput : ")) == 1 :
    #             setup['player'] = "mpv"
    #         else :
    #             setup['player'] = "vlc"
    #         setup['termux'] = input("Are you using Termux ? [y/n] : ") in ('Y','y')
    #         setup['anilist'] = input("Login with anilist ? [y/n] : ") in ('y','Y')
    #         if setup['anilist']:
    #             setup['token'] = anilist.login()
    #             setup['auto'] = input("Auto update anilist after watching anime ? [y/n] : ") in ('y','Y')
    #             setup['username'] = eval(anilist.getUserId(setup['token']).content)['data']['Viewer']['name']
    #         config.write(str(setup))
    #         return setup
firstSetup()
getconfig()
# Closing file
#file_json.close()
#print(f"player: {data['mpv']}")
#print(f"termux : {data['True']}")
#print(f"anilist : {data['False']}")