askName=["What is your name?","atwhay isyay ouryay amenay ? "]
hello = ["Hello","ellohay"]

language = input("What Language do you speak? Pig Latin or English?")
if language.upper() == "ENGLISH":
    choice = 0
elif language.upper() == "PIG LATIN":
    choice = 1
else:
    raise TypeError

name = input(askName[choice])
print(hello[choice] + " " + name)


