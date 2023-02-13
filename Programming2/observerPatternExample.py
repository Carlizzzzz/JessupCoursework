from UI import *

class Independent:
    a = 10
    def Add(self,tmp):
        Independent.a += 1

class Dependent1:
    def __init__(self):
        self.a = Independent.a

    def Update(self):
        if Independent.a != self.a:
            self.a = Independent.a
            print("New Number: "+ str(self.a))

class Dependent2:
    def __init__(self):
        self.a = Independent.a

    def Update(self):
        if Independent.a != self.a:
            print("Last Number: " + str(self.a))

i = Independent()

root = Tk()
f = UIFrame(root=root)
b = UIButton(i.Add, text="Add", bg="green")
f.Add(b, side=LEFT)

d1 = Dependent1()
d2 = Dependent2()

def Update():
    d1.Update()
    d2.Update()
    root.after(10, Update)

root.after(10, Update)
root.mainloop()