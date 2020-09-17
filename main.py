from xml.dom import minidom

file = minidom.parse(r'.\xml.xml')
text = file.getElementsByTagName("text")
print(type(text))
str = ""

for elem in text:
    str = str + elem.childNodes[0].data + "\n"

f = open("./dump.txt", "a+")
f.write(str)
f.close()