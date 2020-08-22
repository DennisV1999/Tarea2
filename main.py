import JsonReader
import XmlReader
import os

def main():
    print("Seleccione el tipo de archivo a leer:\n"+
    "1-Archivo JSON\n"+
    "2-Archivo XML\n"+
    "3-Archivo CSV\n\n")
    arg = input()
    switch(arg)

def Json():
    print("Ingrese una ubicación de archivo Ej: C:\\Usuario\\Archivo.json")
    path = input()
    if not path:
        print("Debe ingresar una ubicación de archivo.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif not path.endswith('.json'):
        print("Debe elegir un archivo con extensión .json")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif not os.path.exists(path):
        print("El archivo no existe.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()    
    else:
        jsonread = JsonReader.JsonReader(path)
        jsonread.fileReader()
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()

def Xml():
    print("Ingrese una ubicación de archivo Ej: C:\\Usuario\\Archivo.xml")
    path = input()
    if not path:
        print("Debe ingresar una ubicación de archivo.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif not path.endswith('.xml'):
        print("Debe elegir un archivo con extensión .json")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif not os.path.exists(path):
        print("El archivo no existe.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()    
    else:
        xmlread = XmlReader.XmlReader(path)
        xmlread.fileReader()
        print("-------------------------------------------------------------")
        print("-------------------------------------------------------------")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()

def Csv():
    input("Csv")

def switch(arg):
    switcher={
        '1': Json,
        '2': Xml,
        '3': Csv
    }
    func = switcher.get(arg, lambda: "Opción Invalida")
    return func()
    
if __name__ == "__main__":
    main()