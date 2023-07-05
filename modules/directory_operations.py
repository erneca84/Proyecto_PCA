import sys, os
import shutil, stat

class DirectorioVacioError(Exception):
    pass
class RutaVaciaError(Exception):
    pass
class DirectorioNoExisteError(Exception):
    pass
class ArchivoNoExisteError(Exception):
    pass

class Directory:
    
    __error = 0

    def __init__(self, directorio, ruta, archivo):
        
        
        try:
            self.set_error(0)

            if directorio == '':
                self.set_error(1)
                raise DirectorioVacioError('El nombre del directorio no puede estar vacio')
            elif ruta == '':
                self.set_error(1)
                raise RutaVaciaError('La ruta no puede estar vacia')
            else:
                self.__directorio = directorio
                self.__ruta = ruta
                self.__archivo = archivo

                self.__path_archivo = os.path.join(self.__ruta , self.__directorio,self.__archivo)
                #if os.path.exists(self.__path_archivo) == False:
                #    raise ArchivoNoExisteError(f'La ruta de archivo especificada {self.__path_archivo}, no existe')
                
                self.__path_directorio = os.path.join(self.__ruta , self.__directorio)

                #if os.path.isdir(self.__path_directorio) == False:
                #    raise DirectorioNoExisteError(f'Directorio especificado {self.__path_directorio}, no existe')

        except DirectorioVacioError as e:
            print(e)

        except RutaVaciaError as e:
            print(e)

       # except ArchivoNoExisteError as e:
       #     print(e)

       # except DirectorioNoExisteError as e:
       #     print(e)

    def get_error(self):
        return self.__error

    def set_error(self,error):
        self.__error = error
        
    def crear_directorio(self,directorio):
        #__path = os.path.join(self.__ruta , self.__directorio)
        self.__path_nuevo_directorio = os.path.join(self.__ruta , directorio)
        try:
            os.mkdir(self.__path_nuevo_directorio)
        except FileExistsError:
            print(f"Directorio {self.__path_nuevo_directorio}, ya existe.")
        except FileNotFoundError: 
            print(f"La ruta especificada no se encuentra {self.__path_nuevo_directorio}")

    def eliminar_directorio(self,directorio):
        self.__path_elimina_directorio = os.path.join(self.__ruta , directorio)
        try:#Si el directorio no contiene arcivos 
            os.rmdir(self.__path_elimina_directorio)
        except FileNotFoundError:
            print(f"El sistema no puede encontrar el directorio especificado {self.__path_elimina_directorio}.") 
        except OSError:#Si el directorio contiene archivos
            shutil.rmtree(self.__path_elimina_directorio)

    def listar_archivos(self):
        try:
            print(os.listdir(self.__path_directorio))    
        except FileNotFoundError:
            print(f"El sistema no puede encontrar el directorio especificado {self.__path_directorio}.")     

    def renombrar_directorio(self,nuevo_directorio):
        self.__nuevo_directorio = os.path.join(self.__ruta , nuevo_directorio)
        try:
            if os.path.isdir(self.__path_directorio) == False:
                    raise DirectorioNoExisteError(f'El directorio especificado {self.__nuevo_directorio}, no existe')
            
            os.rename(self.__path_directorio,self.__nuevo_directorio)
        except FileNotFoundError:
            print(f"El sistema no puede encontrar el directorio especificado {self.__path_directorio}.")         
        except FileExistsError:
            print(f"No se puede crear un directorio que ya existe {self.__nuevo_directorio}")     
        except DirectorioNoExisteError as e:
            print(e)       

    def buscar_archivo(self,archivo):
        self.__buscar = archivo
        self.__directorio = self.__path_directorio#os.getcwd()
        total = 0

        if(len(sys.argv) > 1):
            if(not os.path.isdir(sys.argv[1])):
                print(sys.argv[1],"no se reconoce como directorio")
                sys.exit(1)
            self.__directorio = sys.argv[1]

        for root, dir, ficheros in os.walk(self.__directorio):
            for fichero in ficheros:
                if(self.__buscar in fichero.lower()):
                    print(root+"\\"+fichero)
                    total += 1        
        print("En total hay",total,"archivos con",self.__buscar)

#miclase = Directory_operation('PRUEBA','C:\Ernesto\Python','data.txt')#data.txt
#if miclase.get_error() == 0:
#miclase.crear_directorio()


#miclase.crear_archivo()
#miclase.renombrar_directorio('PRUEBA_renombrar')
#miclase.eliminar_archivo()
#miclase.eliminar_directorio()

#miclase.mover_archivo('C:\Ernesto\Python1')

#miclase = Directory_operation('Python','C:\Ernesto','data.txt')
#miclase.renombrar_archivo('nueva_data_1.txt')

#miclase = Directory_operation('Ernesto','C:\\','data.txt')
#if miclase.get_error() == 0:
#    miclase.buscar_archivo('casa')

#miclase = Directory_operation('Chatbot','C:\Ernesto\Python','')    
#if miclase.get_error() == 0:
#    miclase.listar_archivos()

#miclase.cambiar_permisos_archivo(7,5,5)

