# 1
with open("test.txt", "w") as myfile:
    myfile.write("Hello Ben\n")
    myfile.write("How is your day?\n")
    myfile.write("Did u see a snake today?\n")
    myfile.write("Thank you for the semester!\n")
    myfile.write("God bless!\n")

with open("test.txt", "r") as myfile:
    all_lines = myfile.readlines()

with open("reverse.txt", "w") as reverse:
    for text in reversed(all_lines):
        reverse.write(text)

# 2
with open("snake.txt", "w") as snake:
    for text in all_lines:
        if "snake" in text:
            snake.write(text)

# 3
with open("numbered.txt", "w") as numbered:
    layout = "{0:<4}{1:<0}"
    flag = 1
    for text in all_lines:
        numbered.write(layout.format(flag, text))
        flag += 1

# 4
with open("numbered.txt", "r") as numbered:
    numbered_line = numbered.readlines()

with open("number_remove.txt", "w") as remove:
    i = 1
    for text in numbered_line:
        if text.startswith(str(i)):
            remove.write(text.replace(str(i), "").strip() + "\n")
        else:
            remove.write(text)
        i += 1

# 5
import requests

url = "http://xml.resource.org/public/rfc/txt/rfc793.txt"
response = requests.get(url)
print(response.text)
