def jewelsDetect(jewels,stones):
    flag=0
    for i in jewels:
        for j in stones:
            if i==j:
                flag+=1
    return flag

jewels = "aA"
stones = "acbbbb"
print(jewelsDetect(jewels,stones))