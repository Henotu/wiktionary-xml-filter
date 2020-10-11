from xml.dom import minidom
import io

input_file = input("Please put the path to the xml file here:\n")
input

file = minidom.parse(input_file)
text = file.getElementsByTagName("text")

str = ""

for k, elem in enumerate(text):
    #if text.length % (k+1) == 0:
     #   print((k - 1)/text.length * 100 + "%")
    if int(elem.getAttribute("bytes")) > 0:
        val = elem.firstChild.nodeValue
        if "{{Wortart|Substantiv|Deutsch}}" in val:
            str = str + elem.parentNode.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.previousSibling.firstChild.nodeValue + "\n"

with io.open("./Substantive.txt", "w", encoding="utf-8") as f:
    f.write(str)
f.close()