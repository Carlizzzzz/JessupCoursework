import string

count = {}
s = "'After beating the eggs, Dana read the next step:''Add milk and eggs, then add flour and sugar.'"
s = s.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
s = s.lower()
print(s)
s_list = s.split()
for word in s_list:
    count[word] = count.get(word, 0) + 1

print(count)