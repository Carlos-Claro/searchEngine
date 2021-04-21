import requests
from bs4 import BeautifulSoup

class Engine(object):

    def __init__(self):
        self.arquivo = 'urls.txt'
        self.arquivo_conteudo = 'conteudo.txt'
        self.headers = {'User-Agent': 'Searchtags'}
        lista = self.get_lista()
        for linha in lista:
            self.set_arquivo_conteudo(linha.rstrip())

    def set_arquivo_conteudo(self,url):
        i = self.get_html(url)
        print(';'.join(map(str, i.values())))
        arquivo = open(self.arquivo_conteudo,'a')
        arquivo.writelines([';'.join(map(str, i.values())),'\n'])

    def get_lista(self):
        arquivo = open(self.arquivo, 'r')
        return arquivo.readlines()


    def get_html(self, url):
        try:
            res = requests.get(url, stream=True, headers=self.headers)

        except requests.exceptions.HTTPError as e:
            print("httperror")
            print(e)
        except requests.exceptions.Timeout as t:
            print("timeout")
            print(t)
        except requests.exceptions.SSLError as s:
            print("sslerror")
            print(s)
        except requests.exceptions.ConnectionError as c:
            print("conection error")
            print(c)
        else:
            content = BeautifulSoup(res.content)
            retorno = {}
            retorno['url'] = url
            try:
                ogdescription = content.find("meta",  {"name":"og:description"}).attrs
                retorno['descricao'] = ogdescription['content']
            except:
                pass
            if 'descricao' not in retorno:
                try:
                    description = content.find("meta",  {"name":"description"}).attrs
                    retorno['descricao'] = description['content']
                except:
                    retorno['descricao'] = 'sem description'
            retorno['title'] = content.title.string
            retorno['h1'] = content.h1.string
            return retorno

    def trash(self):
        imoveis = []
        for x in imoveis:
            arquivo.writelines([str(x.h2.string),'\n',str(x.select(".opcionais")),'\n'])
            print(x.h2.prettify())
            print(x.select(".opcionais"))
        print("ok")



if __name__ == '__main__':
    Engine()
