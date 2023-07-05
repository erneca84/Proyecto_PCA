import random
import string
import warnings
import nltk
from nltk.stem import WordNetLemmatizer                                                                            
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Nlp:
    def __init__(self, directory, path_corpus):
        self.sent_tokens = []
        self.GREETING_INPUTS = ("hi", "hello", "greetings", "sup", "what's up", "hey")
        self.GREETING_RESPONSES = ["hey", "hi","*nods*", "hi there", "hello", "I am glad you are chatting with me"]
        self.BOT_NAME = "Fer-Bot"
        self.directory = directory
        self.path_corpus = path_corpus

    def initialize_nlp(self):
        
        warnings.filterwarnings('ignore')
        
        #Bajar vocabulario auxiliar
        #*************************#
        
        #Paquete de datos que contiene modelos y recursos para la tokenización de texto en diferentes idiomas. 
                
        #Popular 
        nltk.download('popular', quiet=True)
        
        #Punkt proporciona reglas y algoritmos para dividir el texto en oraciones
        nltk.download('punkt', quiet=True)
        
        nltk.download('wordnet', quiet=True)

        #Lee el contenido del archivo para tokenizarlo posteriormente
        with open(self.path_corpus, 'r', encoding='utf8', errors='ignore') as fin:
            row = fin.read().lower()

        #Para dividir un texto en oraciones individuales. 
        self.sent_tokens = nltk.sent_tokenize(row)

    def lem_tokens(self, tokens):
        """Lematiza las palabras base (lema): "corriendo", "corre", "corrió" --> "correr".

        Args:
            tokens (list): Lista con palabras o tokens individuales

        Returns:
            (list): Lista con palabras lematizadas
        """
        lemmer = WordNetLemmatizer()
        return [lemmer.lemmatize(token) for token in tokens]

    def lem_normalize(self, text):
               
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        
        #word_tokenize --> divide un texto o una oración en una lista de palabras o tokens individuales.
        #                   "Hello, how are you today?" --> ['Hello', ',', 'how', 'are', 'you', 'today', '?']
        
        #Devuelve un texto normalizado (convierte a minusculas, elimina puntuciación y lematiza)
        return self.lem_tokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    #Retornar un saludo si el suario envia uno
    def greeting(self, sentence):
        for word in sentence.split():
            if word.lower() in self.GREETING_INPUTS:
                return random.choice(self.GREETING_RESPONSES)

    #Procesar el input del usuario, obtener la respuesta y retornarla
    def response(self, user_response):
        bot_response = ''
        
        # Adiciona la respuesta del usuario a la lista de tokens enviados para procesar la similitud
        self.sent_tokens.append(user_response)
        
        #Crea y entrena un modelo de Vectorizador Tf-Idf
        TfidfVec = TfidfVectorizer(tokenizer=self.lem_normalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sent_tokens)
        
        #Obtiene el valor más similar usando metodo de similitud de coseno
        vals = cosine_similarity(tfidf[-1], tfidf)
        
        #Obtiene el índice de respuestas para elegir de la matriz ([-2]: últimos 2 elementos)
        #Respuesta más similar
        idx = vals.argsort()[0][-2]
        
        #Obtiene una copia del array "vals" reducido
        flat = vals.flatten()
        flat.sort()

        #Incluye a la respuesta del bot la cadena de respuesta
        if flat[-2] == 0:
            bot_response = bot_response + "I am sorry, but I don't understand your request"
        else:
            bot_response = bot_response + self.sent_tokens[idx]
        
        #Elimina la respuesta del usuario de la lista de tokens enviados
        self.sent_tokens.remove(user_response)

        return bot_response

    def talk_to_client(self, message):
        print(f"{self.BOT_NAME}: " + message)

    