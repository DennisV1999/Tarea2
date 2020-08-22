import xml.etree.ElementTree as ET

class XmlReader:

    def __init__(self, path):
        self.path = path

    def fileReader(self):
        tree = ET.parse(self.path)
        root = tree.getroot()
        for reg in root:
            print("-------------------------------------------------------------")
            print("-------------------------------------------------------------")
            for subreg in reg:
                print(subreg.tag.capitalize() + ": " + subreg.text)