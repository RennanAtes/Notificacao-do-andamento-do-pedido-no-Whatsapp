import pandas as pd
import openpyxl
import sendMessage
from sqlalchemy import create_engine, text
import urllib
import requests

class Notification():

    def __init__(self):
        engine = create_engine('IPSQL')
        query = text("Filtro")
        conn = engine.connect()
        self.datasSQL =pd.read_sql(query, conn)
        #self.datasSQL = pd.read_excel('planilha.xlsx')
        self.datas = pd.read_excel("SalvarDados.xlsx")


    def obtendoOIDAbsoluto(self,i): 
        #Obtendo o ID unico do cliente, que está no SQL
        self.idAbsoluto = self.datasSQL.loc[i][35]


    def collectDatesID(self):
        self.indiceIDAbsolut = (self.datasSQL.index[self.datasSQL['id'] == self.idAbsoluto].tolist())

        # Indices dos dados do SQL
        self.DatesOfIDSQL = {
            'idPedido': self.datasSQL.loc[self.indiceIDAbsolut[0]][0],
            'nome' : self.datasSQL.loc[self.indiceIDAbsolut[0]][8],
            'statusPedido' : self.datasSQL.loc[self.indiceIDAbsolut[0]][2],
            'telefone' : self.datasSQL.loc[self.indiceIDAbsolut[0]][18],
            'nameproduct' : self.datasSQL.loc[self.indiceIDAbsolut[0]][37],
            'transportadora' : self.datasSQL.loc[self.indiceIDAbsolut[0]][23],
            'urlrastreio' : self.datasSQL.loc[self.indiceIDAbsolut[0]][25],
            'pricetotal' : self.datasSQL.loc[self.indiceIDAbsolut[0]][4],
            'idPedidoLoja': self.datasSQL.loc[self.indiceIDAbsolut[0]][34]
        }

    def sicronizandoIDAbsoluto(self,a):
        
        self.OrderPlanilhaTeste = (self.datas.index[self.datas['idPedidoMarketplace'] == self.idAbsoluto].tolist())
        if self.OrderPlanilhaTeste == []:
            Notif.collectDatesID()
            dados = {'idPedido':self.DatesOfIDSQL['idPedido'],
            'nome':self.DatesOfIDSQL['nome'],
            'telefone':self.DatesOfIDSQL['telefone'],
            'statusPedido':self.DatesOfIDSQL['statusPedido'],
            'transportadora':self.DatesOfIDSQL['transportadora'],
            'idPedidoMarketplace':self.idAbsoluto
            }
            print("Enviar a mensagem")
            Notif.EnviarMensagem()
            nova_linha = pd.DataFrame(dados, index=[0])
            self.datas = pd.concat([self.datas, nova_linha], ignore_index=True)



    def CollectDatesSalvar(self):
        print(self.indiceIDAbsolut)
        self.indiceIDAbsolutSalvar = (self.datas.index[self.datas['idPedidoMarketplace'] == self.idAbsoluto].tolist())
        self.DatesOfIDSalvar = {
            'idPedido': self.datas.loc[self.indiceIDAbsolutSalvar[0]][0],
            'nome' : self.datas.loc[self.indiceIDAbsolutSalvar[0]][1],
            'statusPedido' : self.datas.loc[self.indiceIDAbsolutSalvar[0]][3],
            'telefone' : self.datas.loc[self.indiceIDAbsolutSalvar[0]][2],
            'transportadora' : self.datas.loc[self.indiceIDAbsolutSalvar[0]][4],
        }
    
    def indices(self):
        qt = len(self.datasSQL)
        return qt
    def Verificando(self):
        print(self.DatesOfIDSQL['statusPedido'])
        print(self.DatesOfIDSalvar['statusPedido'])

        if self.DatesOfIDSQL['statusPedido'] != self.DatesOfIDSalvar['statusPedido']:
            Notif.EnviarMensagem()
            self.datas.loc[self.indiceIDAbsolutSalvar[0], 'statusPedido']= self.DatesOfIDSQL['statusPedido']
            

    def SalvarDados(self):
        self.datas.to_excel('SalvarDados.xlsx', index = False)

    def lerOPandasNovamente(self):
        self.datas = pd.read_excel("SalvarDados.xlsx")

    def EnviarMensagem(self):
        if not self.DatesOfIDSQL['telefone'] == '':
            sendMessage.EnviarMensagem(
            #self.DatesOfIDSQL['telefone'],
            '41998891464',
            self.DatesOfIDSQL['statusPedido'],
            self.DatesOfIDSQL['nome'],
            'Pagamento',
            self.DatesOfIDSQL['nameproduct'],
            self.DatesOfIDSQL['pricetotal'],
            self.DatesOfIDSQL['transportadora'],
            self.DatesOfIDSQL['urlrastreio'],
            )


def check_internet():
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.exceptions.ConnectionError:
        return False



Internet = check_internet() #Verificando a internet
if Internet: 
    Notif = Notification()
    looping = Notif.indices()

    for i in range (0,looping): #Sicronizar os dados, o SQL com o SalvarDados
        Internet = check_internet() #Verificando a internet a cada looping.
        if Internet:
            Notif.obtendoOIDAbsoluto(i)
            Notif.sicronizandoIDAbsoluto(i)

    for b in range(0,looping): # Olhar se algum pedido está diferente, e enviar a mensagem!
        if Internet:
            Notif.obtendoOIDAbsoluto(b)
            Notif.collectDatesID()
            Notif.CollectDatesSalvar()
            Notif.Verificando()
    Notif.SalvarDados()