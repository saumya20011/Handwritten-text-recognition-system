#!C:\Users\HP\AppData\Local\Programs\Python\Python36\python.exe

print("content-type:text/html")
print("")

from code import loadFile

menu = loadFile("menu.html")
home = loadFile("index.html")
footer = loadFile("footer.html")

data = menu + home + footer

print(data)
