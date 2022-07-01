from pypresence import Presence
from enum import Enum
# local

#MAIN PROGRAM

dcrpc = False;
try:
    client_id = "926022094976852038"  
    RPC = Presence(client_id=client_id)
    RPC.connect()
    dcrpc = True
except:
    print("Can't Connect to discord")

def mainMenuState():
    if dcrpc:
        RPC.update(state="In Main Menu", details="Browsing anime") #update dict
def resumeState():
    if dcrpc:   
        RPC.update(state="Resume Watching", details="Select Config") #update dict
def historyState():
    if dcrpc:
            RPC.update(state="History", details="Manage History") #update dict
def recentlyState():
    if dcrpc:
            RPC.update(state="Recently Uploaded", details="Select Title") #update dict
def searchState():
    if dcrpc:
        RPC.update(state="Anime Lists", details="Select Title") #update dict
def DetailsState():
    if dcrpc:
        RPC.update(state="Details", details="Select Episode") #update dict


# from typing_extensions import Self
class State(Enum):
    MAIN_MENU = 0
    HISTORY = 1
    RESUME = 2
    RECENTLY = 3

class Trigger(Enum):
    mm = 0
    h = 1
    r = 2
    a = 3

class transition():
    prevState : State
    nextState : State
    trigger : Trigger

    def __init__(self,prevState, nextState, trigger):
        self.prevState = prevState
        self.nextState = nextState
        self.trigger = trigger

p : transition = [transition(State.MAIN_MENU, State.HISTORY, Trigger.h),
                    transition(State.MAIN_MENU, State.RESUME, Trigger.r),
                    transition(State.MAIN_MENU, State.RECENTLY, Trigger.a)
                ]

currentState : State = "MAIN_MENU"
RPC.update(state=currentState, details="Browsing anime")
def getNextState(prevState:State, trigger:Trigger):
    nextState : State = prevState
    i = 0
    for i in range(len(p)):
        if p[i].prevState.name == prevState and p[i].trigger.name == trigger:
            nextState = p[i].nextState
    return nextState

def activeTrigger(trigger:Trigger):
    global currentState
    nextState:State = getNextState(currentState, Trigger[trigger].name)
    currentState = nextState
    RPC.update(state=currentState, details="Browsing anime") #update dict

# # https://www.guru99.com/variables-in-python.html

# print("Current State: ",currentState)
# y =  str.lower(input("Pindah State ke: "))
# activeTrigger(y)
# print("Current State: ",currentState.name)

# panggil fungsi di dcrpc, inputan tiap state terdapat pada tiap window