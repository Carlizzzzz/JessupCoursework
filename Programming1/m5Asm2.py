
# 1
def readAlphabet(str):
    sentence = ""
    sentence = sentence.join(str.split()).lower()
    temp = []
    temp[:0] = sentence
    temp.sort()
    letterCount = {}
    for i in temp:
        letterCount[i] = letterCount.get(i, 0) + 1
    for x in letterCount:
        print(x, "", letterCount[x])


str = "ThiS is String with Upper and lower case Letters"
readAlphabet(str)


# 2
##a 35
##b 4
##c True
##d Error
##e 0
##f apple banana grapes orange
##g False

def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return None


# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)
print("strawberries" in new_inventory)
print(new_inventory["strawberries"] == 10)
add_fruit(new_inventory, "strawberries", 25)
print(new_inventory["strawberries"] == 35)


# 3
def removeStuff(str):
    punctuations = '''1234567890!()[]{};—:'"“”‘’\,<>./?@#$%^&*_~'''  #remove all unwanted symbols
    for char in punctuations:
        str = str.replace(char, " ")

    return str

file = open("D:\Alice.txt", "r", encoding="utf-8")
result = open("alice_words.txt", "w+", encoding="utf-8")
str = removeStuff(file.read()).lower()
content = str.split()
content.sort()
words = {}
layout = "{0:<20}{1:<0}{2:<0}"
result.write(layout.format("Word","Count","\n"))
result.write("="*25+"\n")
for i in content:
    words[i] = words.get(i, 0) + 1
for x in words:
    result.write(layout.format(x, words[x],"\n"))
print("Alice appeared",words.get("alice"),"times in the book")
result.close()


#4
flag = ""
for x in words:
    if len(x)>len(flag):
        flag = x
print(flag, "is the longest word")

#Sets
fav_Band = {"Maroon 5","Beyond","Imagine Dragon","Coldplay","The Beatles"}
print(fav_Band)
fav_Band.add("Monsta X")
print(fav_Band)
fav_Band.add("Stray Kids")
print(fav_Band)
fav_Band.add("ABBA")
print(fav_Band)
#They are not in order. The added item is randomly inserted.