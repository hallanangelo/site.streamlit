import requests
import time
from bs4 import BeautifulSoup 


fundos = ['PRSN11B', 'SCPF11', 'CEOC11','MFAI11','FIIB11']	


for i in fundos:
    site = "https://www.fundsexplorer.com.br/funds/" + i
    html = requests.get(site).content
    dados = BeautifulSoup(html, 'html.parser')

    porcentagem = dados.find("span", class_ ="percentage positive")
    ultimo_rendimento = dados.find_all("span", class_ ="indicator-value")
    nome = dados.find("h1", class_ ="section-title" )

    print(nome.text, ': ',ultimo_rendimento[1].text[20:])
    



