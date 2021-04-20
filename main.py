import requests
from bs4 import BeautifulSoup

class Engine(object):

    def __init__(self):
        self.url = "https://www.zapimoveis.com.br/aluguel/apartamentos/pr+curitiba/"
        self.headers = {'User-Agent': 'Portaisimobiliarios.com.br - quero seus dados'}

    def get_html(self):
        try:
            res = requests.get(self.url, stream=True, headers=self.headers)

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
            print(res.status_code)
            content = BeautifulSoup(res.content)
            print(content.find("meta",  {"name":"og:description"}))
            exit()
            # print(content.prettify())
            imoveis = content.select(".imovel")
            arquivo = open('teste.txt','a')

            for x in imoveis:
                arquivo.writelines([str(x.h2.string),'\n',str(x.select(".opcionais")),'\n'])
                print(x.h2.prettify())
                print(x.select(".opcionais"))
        print("ok")



if __name__ == '__main__':
    Engine().get_html()
