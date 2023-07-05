import matplotlib.pyplot as plit
import pandas as pd

class chart():
    def __init__(self,nit_filtro_data):
       self.__nit_filtro_data = int(nit_filtro_data)

    def graficar(self):
        
        df = pd.read_csv('C:\\Ernesto\\Python\\chatbot\\data\\data_processed.csv',header=0 ,usecols=['valor_contrato','fecha_de_firma_del_contrato','nit_de_la_entidad'])

        #df.head(5)

        #filtro_nit = self.__nit_filtro_data #804003933
        nit = df['nit_de_la_entidad'] == self.__nit_filtro_data#filtro_nit
        #nit.head()
        filtrado_por_nit = df[nit]
        #filtrado_por_nit.head()

        df1 = filtrado_por_nit.groupby(['fecha_de_firma_del_contrato'])[['valor_contrato']].sum()

        colors  = ("dodgerblue","salmon", "palevioletred", 
                "steelblue", "seagreen", "plum", 
                "blue", "indigo", "beige", "yellow")

        df1.plot(kind='bar',cmap='Paired',color="dodgerblue",title="Valor Contrato firmado por año y mes",ylabel="Valores contrato",xlabel="Fecha de Firma",legend="")

        plit.waitforbuttonpress()
        plit.show()
        #plit.savefig('ImagenPrueba.pdf')

#migafica = chart(804003933)       
#migafica.graficar() 
