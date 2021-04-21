# ######################################
# Buscador de termos no google para pesquisas de concorrencia
#
# https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
# ######################################
import requests
import json

class googleSearch(object):

    def __init__(self):
        self.url = 'https://customsearch.googleapis.com/customsearch/v1'
        self.key = self._get_keys()
        self.headers = {'User-Agent': 'PowInternet'}

    def _get_keys(self):
        endereco = '/var/www/json/keys.json'
        with open(endereco) as json_file:
            data = json.load(json_file)
            return data['google_keys']['search']

    def get(self):
        url = '{}?key={}&q={}&cx={}'.format(self.url,self.key,'imoveis em curitiba','005615536511216203443:axucwrkrwgo')
        print(url)
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
            print(res.status_code)
            print(json.load(res.content))

if __name__ == '__main__':
    googleSearch().get()
