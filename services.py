#!C:\Users\HP\AppData\Local\Programs\Python\Python36\python.exe 

print("content-type:text/html")
print("")



import cgi, os
import cgitb
import os
from code import loadFile

import sys
sys.path.insert(0, "HTR\src")
import main

cgitb.enable()



msg = "Please Enter First"
menu = loadFile("menu.html")
services = loadFile("services.html")
footer = loadFile("footer.html")

form = cgi.FieldStorage()
fileitem = form['file']

os.remove("HTR/data/test.png")

try:
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('HTR/data/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'

else:
    message = 'No file was uploaded'

old = "HTR/data/" + fn
os.rename(old,"HTR/data/test.png")

msg = main.run()

data = menu + services.format(rec_msg=msg) + footer
print(data)





