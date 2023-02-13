def reverse_words(message):
    temp = ""
    temp_List = temp.join(message).split()
    print(temp_List[::-1])


message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']
reverse_words(message)
