import nltk
from modules.natural_language_processing import Nlp
from modules.directory_operations import Directory
from modules.file_operations import File
import os
from charts.chart_generation import chart


def run_chatbot(chat):
    """
        Manejador de ejecución de chatbot haciendo uso de modelos implementados
        
        Args: 
            chat (str): Objeto instanciado de la clase Nlp   
            
        Returns:
            None
    """
               
    try:
        flag = True
        chat.talk_to_client(f"My name is {chat.BOT_NAME}. I will answer your queries about file and directory manipulation .")
        while flag:
            chat.talk_to_client("Please type a request about files and directories. If you want to exit, type Bye!")
            user_response = input()
            if "bye" in user_response.lower():
                flag = False
                chat.talk_to_client("Bye! take care..")
            elif "thank" in user_response.lower():
                flag = False
                chat.talk_to_client("You are welcome..")
            elif chat.greeting(user_response) is not None:
                chat.talk_to_client(chat.greeting(user_response))
            else:
                tokens = nltk.word_tokenize(user_response)
                chat.talk_to_client(chat.response(user_response))
                if 'list files' in user_response:
                    #print(chat.directory.list_files())
                    chat.directory.listar_archivos()
                elif 'create file' in user_response:
                    name = tokens[tokens.index('file') + 1]
                    file = File(chat.directory._Directory__directorio,chat.directory._Directory__ruta,name)
                    file.crear_archivo()
                    
                elif 'create directory' in user_response:
                    name = tokens[tokens.index('directory') + 1]
                    chat.directory.crear_directorio(name)
                    #chat.directory.create_directory(name)
                elif 'delete directory' in user_response:
                    name = tokens[tokens.index('directory') + 1]
                    chat.directory.eliminar_directorio(name)
                    #chat.directory.create_directory(name)                    
                elif 'rename directory' in user_response:
                    new_name = tokens[tokens.index('to') + 1]
                    #chat.directory.rename_directory(new_name)   
                    chat.directory.renombrar_directorio(new_name)
                elif 'rename' in user_response:
                    old_name = tokens[tokens.index('rename') + 1]
                    new_name = tokens[tokens.index('to') + 1]
                    file = File(chat.directory._Directory__directorio,chat.directory._Directory__ruta,old_name)
                    file.renombrar_archivo(new_name)                    
                    #file = File(os.path.join(chat.directory.path, old_name))
                    #file.rename(os.path.join(chat.directory.path, new_name))                    
                elif 'delete file' in user_response:
                    name = tokens[tokens.index('file') + 1]
                    file = File(chat.directory._Directory__directorio,chat.directory._Directory__ruta,name)
                    file.eliminar_archivo()

                    #file = File(os.path.join(chat.directory.path, name))
                    #file.delete()
                elif 'search' in user_response or 'find' in user_response or 'lookup' in user_response:
                    search_keywords = ['search', 'find', 'lookup']
                    
                    name = tokens[tokens.index(next((word for word in tokens if word in search_keywords), None)) + 1] if any(word in tokens for word in search_keywords) else None
                    file = File(chat.directory._Directory__directorio,chat.directory._Directory__ruta,name)
                    file.buscar_archivo(name)

                    #matches = chat.directory.search_file(name)
                    #print( f'Se encontraron los siguientes archivos: {", ".join(matches)}')
                elif 'move file' in user_response:
                    tokens = user_response.split()
                    # Encontrar los índices de las palabras clave "file" y "to"
                    move_index = tokens.index("file")
                    to_index = tokens.index("to")
                    file_path = " ".join(tokens[move_index + 1:to_index])
                    destination_path = " ".join(tokens[to_index + 1:])

                    #print(file_path)
                    #print(destination_path)
                    file = File(chat.directory._Directory__directorio,chat.directory._Directory__path_directorio,chat.directory._Directory__path_archivo)
                    file.mover_archivo(file_path,destination_path)

                    #chat.directory.move_file(file_path, destination_path)
                elif 'change permissions' in user_response:
                    tokens = user_response.split()
                    # Encontrar los índices de las palabras clave "move" y "to"
                    name = tokens.index("permissions")
                    to_index = tokens.index("to")
                    file_path = " ".join(tokens[name + 1:to_index])
                    name = tokens[tokens.index('permissions') + 1]
                    permissions = int(" ".join(tokens[to_index + 1:]), 8)
                    file = File(chat.directory._Directory__directorio,chat.directory._Directory__ruta,name)
                    file.cambiar_permisos_archivo(permissions)
                elif 'graphic' in user_response:
                    entity_select = tokens[tokens.index('entity') + 1]
                    grafica = chart(entity_select)
                    grafica.graficar()
    except LookupError as err:
        print ('Tenemos un error',err)    
        
#print(__name__)

if __name__ == '__main__':
    
    #directory_path = r'D:\AM\chatbot\data\data_test'

    directory_path = r'C:\Ernesto\Python'

    #print(directory_path)

    #obtener la ruta absoluta del directorio.
    absolute_path = os.path.abspath(directory_path)
    
    #Instanciando objeto de tipo Directory
    #directory = Directory(absolute_path)
    directory = Directory('PRUEBA',absolute_path,'')
    
    #miclase = Directory_operation('PRUEBA','C:\Ernesto\Python','data.txt')#data.txt
    
    #Ruta con corpus usado para entrenar el modelo
    path_corpus = 'C:\\Ernesto\\Python\\chatbot\\modules\\files_directories.txt'
    
    #Instanciando objeto de tipo Nlp
    chatbot = Nlp(directory, path_corpus)
    print('Intanciado objeto')
    chatbot.initialize_nlp()
    print('Inicializado modulo nlp')
    run_chatbot(chatbot)
    print('Chat finalizado')