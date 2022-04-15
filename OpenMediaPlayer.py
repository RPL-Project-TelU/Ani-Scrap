import os
import enum

def firstSetup():
    try:
        with open('./kaasi.txt','r',encoding='utf-8') as config:
            return eval(config.read())
    except:
        with open('./kaasi.txt','w',encoding='utf-8') as config:
            setup = {}
            print("First time setup")
    # membuat class enum untuk tab
    class Player(enum.Enum):
        mvp = 1
        vlc = 2

      
        # # printing enum member as string
        # print ("The string representation of enum member is : ",end="")
        # print (Player.mvp)
 
        # # printing enum member as repr
        # print ("The repr representation of enum member is : ",end="")
        # print (repr(Player.mvp))
 
        # # printing the type of enum member using type()
        # print ("The type of enum member is : ",end ="")
        # print (type(Player.mvp))
 
        # # printing name of enum member using "name" keyword
        # print ("The name of enum member is : ",end ="")
        # print (Player.mvp.mvp)



        # # printing enum member as string
        # print ("The string representation of enum member is : ",end="")
        # print (Player.vlc)
 
        # # printing enum member as repr
        # print ("The repr representation of enum member is : ",end="")
        # print (repr(Player.vlc))
 
        # # printing the type of enum member using type()
        # print ("The type of enum member is : ",end ="")
        # print (type(Player.vlc))
 
        # # printing name of enum member using "name" keyword
        # print ("The name of enum member is : ",end ="")
        # print (Player.vlc.vlc)
    
