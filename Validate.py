#!C:\Users\HP\AppData\Local\Programs\Python\Python36\python.exe

print("content-type:text/html")
print("")

from code import loadFile

menu = loadFile("menu.html")
valid = loadFile("validate.html")
footer = loadFile("footer.html")

data = menu + valid + footer

print(data)
