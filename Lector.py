#from tkinter.tix import Tree
import xml.etree.cElementTree as ET
from Paciente import Paciente
#class Lector():




def cargarArchivo():
    archivo= ET.parse("Tarea1.xml")
    raiz=archivo.getroot()
    lista=[]
   # print(raiz)
    contador=0 
    for elem in raiz:
        for subelem in elem:
            for subsubelem in subelem.iter('datospersonales'):
               
               for subsubelem2 in subsubelem.iter('nombre'):
                nombre=subsubelem2.text
                
                print(nombre)
               for edad in subsubelem.iter('edad'):
                 edad=edad.text
                 print(edad)
               paciente=Paciente(nombre,edad)
               lista.append(paciente)
              
            for periodo in subelem.iter('periodos'):
                print("periodos: "+ periodo.text)
            for m in subelem.iter('m'):
                matriz=m.text
                print("matriz: "+ matriz)
            for reja in subelem.iter('rejilla'):
                 for celda in reja.iter('celda'):
                    f=celda.attrib['f']
                    c=celda.attrib['c']
                    print("filas "+f+"columnas "+c)
                 print("*********************")
            
         

cargarArchivo() 

    