from tkinter.tix import Tree
import xml.etree.cElementTree as ET

#class Lector():
archivo= ET.parse("Tarea1.xml")
raiz=archivo.getroot()

print(raiz)

for x in raiz:
    print(x)
       