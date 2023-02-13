from abc import ABC, abstractmethod
end = False

def validate(action):
    if isinstance(action, str):
        if action.upper() in ["IGNORE", "PET", "PLAY", "FEED", "TAKE ON WALK"]:
            return True
        elif action.upper() == "END":
            global end
            end = True
        else:
            raise IndexError
    else:
        raise TypeError


class BaseState(ABC):
    currentState = None
    stateList = {}

    @classmethod
    def NextState(cls, name):
        if name in cls.stateList:
            cls.currentState = cls.stateList[name]
            cls.currentState.EnterState()

    def __init__(self, name):
        self.name = name
        BaseState.stateList[name] = self

    @abstractmethod
    def Message(self):
        print("\nDoggy is now " + self.name)

    @abstractmethod
    def EnterState(self):
        pass

class Sleeping(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Sleeping")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Sleeping")
            elif action.upper() == "PET":
                BaseState.NextState("Greeting")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Barking")

    def EnterState(self):
        BaseState.EnterState(self)

class Idle(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Idle")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Wanting Attention")
            elif action.upper() == "PET":
                BaseState.NextState("Greeting")
            elif action.upper() == "PLAY":
                BaseState.NextState("Playing")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Hungry")

    def EnterState(self):
        BaseState.EnterState(self)

class Greeting(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Greeting")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Wanting Attention")
            elif action.upper() == "PET":
                BaseState.NextState("Barking")
            elif action.upper() == "PLAY":
                BaseState.NextState("Playing")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Hungry")

    def EnterState(self):
        BaseState.EnterState(self)

class WantingAttention(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Wanting Attention")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Barking")
            elif action.upper() == "PET":
                BaseState.NextState("Playing")
            elif action.upper() == "PLAY":
                BaseState.NextState("Playing")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Hungry")

    def EnterState(self):
        BaseState.EnterState(self)

class Playing(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Playing")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "FEED":
                BaseState.NextState("Eating")
            elif action.upper() == "TAKE ON A WALK":
                BaseState.NextState("Hungry")
            else:
                BaseState.NextState("Playing")

    def EnterState(self):
        BaseState.EnterState(self)

class Hungry(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Hungry")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Barking")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Hungry")

    def EnterState(self):
        BaseState.EnterState(self)

class Eating(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Eating")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Wanting to potty")

    def EnterState(self):
        BaseState.EnterState(self)

class WantingToPotty(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Wanting to potty")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            BaseState.NextState("Pottying")

    def EnterState(self):
        BaseState.EnterState(self)

class Pottying(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Pottying")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "PET" or "PLAY":
                BaseState.NextState("Fighting")
            else:
                BaseState.NextState("Idle")

    def EnterState(self):
        BaseState.EnterState(self)

class Barking(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Barking")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Fighting")
            elif action.upper() == "PET":
                BaseState.NextState("Greeting")
            elif action.upper() == "PLAY":
                BaseState.NextState("Playing")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Hungry")

    def EnterState(self):
        BaseState.EnterState(self)

class Fighting(BaseState):
    def __init__(self):
        BaseState.__init__(self, "Idle")

    def Message(self):
        BaseState.Message(self)
        action = input("What are you going to do?")
        if validate(action):
            if action.upper() == "IGNORE":
                BaseState.NextState("Idle")
            elif action.upper() == "PET":
                BaseState.NextState("Idle")
            elif action.upper() == "PLAY":
                BaseState.NextState("Playing")
            elif action.upper() == "FEED":
                BaseState.NextState("Eating")
            else:
                BaseState.NextState("Hungry")

    def EnterState(self):
        BaseState.EnterState(self)

sleep = Sleeping()
idle = Idle()
greeting = Greeting()
attention = WantingAttention()
play = Playing()
hungry = Hungry()
eat = Eating()
wantpotty = WantingToPotty()
potty = Pottying()
bark = Barking()
fight = Fighting()
BaseState.currentState = idle

while not end:
    BaseState.currentState.Message()