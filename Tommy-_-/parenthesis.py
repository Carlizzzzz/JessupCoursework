start = 10
sentence = "Sometimes (when I nest them (my parenthetical) too much (like this (and this))) they get confusing."


def findEnd(sentence, start):
    count = 0
    flag = False
    for i in range(start, len(sentence)):
        if sentence[i:i + 1] == "(":
            count += 1
            flag = True
            print(count,"at" , i)

        if sentence[i:i + 1] == ")":
            count -= 1
            print(count,"at" , i)
        if flag and count == 0:
            return i


print(findEnd(sentence, start))
