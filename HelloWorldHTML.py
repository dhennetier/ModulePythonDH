# write-html-2-windows.py

# hello World verssion Texte puis version web 
fichier = open("hello.txt", "w")
fichier.write("Hello, world!")
fichier.close()


import webbrowser
f = open('helloworld.html','w')
message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""
f.write(message)
f.close()
webbrowser.open_new_tab('helloworld.html')