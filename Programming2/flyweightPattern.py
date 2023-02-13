class String:
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def showDescription(self):
        print(self.name + ": " + self.description)

    def setDescription(self, newDes):
        self.description = newDes


stringTag = ""
stringValue = ""
flag = False
storage = {}
while not flag:
    stringTag = input("What is the string tag?")
    if stringTag.upper() == "exit program":  # exit
        flag = True
        break
    stringValue = input("What is the string value?")
    if stringTag not in storage:
        storage[stringTag] = String(stringTag,stringValue)
    else:
        if stringValue == storage.get(stringTag).description:
            print("Already exist")
        else:
            storage.get(stringTag).setDescription(stringValue)
            print("Value updated")

for i in storage.values():
    i.showDescription()
