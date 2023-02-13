import string

##String
# 2
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'Q' or letter == 'O':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# 3
def count_letters(word, letter):
    count = 0
    for flag in word:
        if flag == letter:
            count += 1
    return count


print(count_letters("banana", "a"))


# 5
def remove_punctuation(phrase):
    result = ""
    for letter in phrase:
        if letter not in string.punctuation:
            result += letter
    return result


def e_finder(paragraph):
    count = 0
    para_list = remove_punctuation(paragraph).split()
    for i in range(len(para_list)):
        if "e" in para_list[i]:
            count += 1
    percentage = round(count / len(para_list) * 100, 1)
    print("Your text contains", len(para_list), " words, of which ", count, "(", percentage, "%)", "contain an 'e'.")


paragraph = "Assign to a variable in your program a triple-quoted string that contains your favour " \
            "Write paragraph of text — perhaps a poem, a speech, instructions to bake a cake, some inspirational " \
            "verses, etc." \
            "Write a function which removes all punctuation from the string, breaks the string into a list of " \
            "words, " \
            "and counts the number of words in your text that contain the letter “e”. Your program should print " \
            "an analysis of the text like this: "
e_finder(paragraph)

# 6
layout0 = "{0:>8}{1:>4}{2:>4}{3:>4}{4:>4}{5:>4}{6:>4}{7:>4}{8:>4}{9:>4}{10:>4}{11:>4}"
print(layout0.format("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print("  :-------------------------------------------------")
layout1 = "{0:>4}"
for i in range(12):
    print(layout1.format(str(i + 1) + ": "), end="")
    for j in range(12):
        print(layout1.format(str((i + 1) * (j + 1))), end="")
    print()


# 7
def reverse(word):
    word = word[::-1]
    return word


print(reverse("happy") == "yppah",
      reverse("Python") == "nohtyP",
      reverse("") == "",
      reverse("a") == "a")


##List
# 4
# Test 1: False
# Since originally, this and that are 2 objects with same value. So they are not the same object. Hence it's false
# Test 2: True
# Then the line"that = this" makes both variables refer to 1 object. Hence it's true

# 6
def scalar_mult(scalar, vector):
    for i in range(len(vector)):
        vector[i] *= scalar
    return vector


print(scalar_mult(5, [1, 2]) == [5, 10],
      scalar_mult(3, [1, 0, -1]) == [3, 0, -3],
      scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
