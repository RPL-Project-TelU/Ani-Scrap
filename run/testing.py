from enum import Enum
# from typing_extensions import Self
class State(Enum):
    MAIN_MENU = 0
    HISTORY = 1
    RESUME = 2
    RECENTLY = 3

class Trigger(Enum):
    DPRC = 0
    h = 1
    r = 2
    a = 3

# a = Trigger    #menggunakan index sbg penelusuran
# s = str(input())
# print(a(1).name)
# print(a.h.name == "h")
# g = "h"      #menggunakan hash value sbg indetify
# print(a[g].name)
# print(a[s].name)

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
                    #transition(State.MAIN_MENU, State., Trigger.DPRC),
                ]
# print(p[0].nextState)
# i = 0
# for i in range(len(p)):
#     print(p[i].prevState)

currentState : State = "MAIN_MENU"
def getNextState(prevState:State, trigger:Trigger):
    nextState : State = prevState
    i = 0
    for i in range(len(p)):
        if p[i].prevState.name == prevState and p[i].trigger.name == trigger:
            nextState = p[i].nextState
    return nextState

# print(p[0].prevState.name == currentState)
# print(type(getNextState("MAIN_MENU","h").name))

def activeTrigger(trigger:Trigger):
    global currentState
    nextState:State = getNextState(currentState, Trigger[trigger].name)
    currentState = nextState

# https://www.guru99.com/variables-in-python.html
# g:Trigger = "h"
# print(Trigger.g)
print("Current State: ",currentState)
y =  str.lower(input("Pindah State ke: "))
# y = "h"
activeTrigger(y)
print("Current State: ",currentState.name)


# r = [transition("MAIN_MENU","HISTORY","h")]
# print(r[0].prevState)
# print(r[0].nextState)
# print(r[0].trigger)

# class clas:
#     a = 1
# r = [clas()]
# print(r[0])

# p = [1,2,3]
# print(p[2])
# p = transition()
# p.transition("MAIN_MENU","HISTORY","h")
# print(p.prevState,)
# print(p.nextState,)
# print(p.trigger,"\n\n\n")
        

# a = State
# # s = str(input())
# print(a(1).name)
# print(a.ALL.name == "ALL")

# while True:

# print(a.value)
# for s in a:
#     print(s)
    # s = str(input())
# class state(Enum):
#     RED = "red"
#     BLUE = "blue"
#     GREEN = "green"
# print(repr(state.RED))
# colo = state
# print(colo)
# print(colo.RED)
# print(colo.RED.name)
# print(colo.RED.value)
