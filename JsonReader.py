import json

class JsonReader:
    
    def __init__(self, path):
        self.path = path
    
    def fileReader(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data['personas']:
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                print("Nombre: "+ regs['nombre'])
                print("Edad: "+ str(regs['edad']))
                print("Estudiante: "+ str(regs['esEstudiante']))
                print("Facultad: "+ regs['facultad'])
