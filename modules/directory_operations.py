import os
import shutil

class Directory_operation:
    

    def __init__(self) -> None:
        pass

    def crear_directorio(self,directorio, ruta):
        path = os.path.join(ruta, directorio)
        try:
            os.mkdir(path)
        except FileExistsError:
            print("Directorio a crear ya existe.")

    def crear_archivo(self, archivo):
        f = open(archivo,"w")
        #f.write(tabla)
        f.close()

    def eliminar_directorio(self,directorio):
        try:
            os.rmdir(directorio)
        except:
            print("Error eliminando directorio.")

    def mover_archivo(self):
        pass    

    def buscar_archivo(self):
        pass        


miclase = Directory_operation.crear_directorio('PRUEBA','./Ernesto/Python')