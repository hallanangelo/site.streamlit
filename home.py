import streamlit as st
from streamlit_player import st_player
import time 

st.set_page_config(page_title="Lóterica")

st.title('Lóterica')
st.code('''import math 

class No:
  def __init__(self, nome, valor):
    self.anterior = None
    self.proximo = None 
    self.nome = nome 
    self.valor = valor 


class Caixa: 
  def __init__(self):
    self.cabeca = None 
    self.tamanho = 0
    self.final = None
    self.dinheiro = 0
  
  def inserir(self, nome, valor):
    if self.tamanho == 0:
      self.cabeca = No(nome, valor)
      self.final = self.cabeca
      self.tamanho += 1
    else:
      ponteiro = self.cabeca
      while ponteiro.proximo:
        ponteiro = ponteiro.proximo
      ponteiro.proximo = No(nome, valor)
      ponteiro.proximo.anterior = ponteiro
      self.final = ponteiro.proximo
      self.tamanho += 1
  
  def proximo(self):
    self.dinheiro += float(self.cabeca.valor)
    ponteiro = self.cabeca
    self.cabeca = ponteiro.proximo
    ponteiro.proximo = None 
    self.tamanho -= 1
  
  def remover(self):
    ponteiro = self.final 
    self.final = ponteiro.anterior 
    ponteiro.anterior = None 
    self.tamanho -= 1 

caixa1 = Caixa() 
caixa2 = Caixa() 

fim_do_loop = True
while fim_do_loop:
  comando = input().split(' ')
  if comando[0] == 'FIM':
    fim_do_loop = False
    print(f'Caixa 1: R$ {caixa1.dinheiro:.2f}, Caixa 2: R$ {caixa2.dinheiro:.2f}')
  elif comando[0] == 'ENTROU:':
    if comando[2] == '1':
      caixa1.inserir(comando[1], float(comando[3]))
      print(f'{comando[1]} entrou na fila 1')
    else:
      caixa2.inserir(comando[1], float(comando[3]))
      print(f'{comando[1]} entrou na fila 2')
  elif comando [0] == 'PROXIMO:':
    if comando[1] == '1':
      if caixa1.tamanho > 0:
        print(f'{caixa1.cabeca.nome} foi chamado para o caixa 1')
        caixa1.proximo()
      else:
        for i in range(caixa2.tamanho - math.ceil(caixa2.tamanho/2)):
          caixa1.inserir(caixa2.final.nome, caixa2.final.valor)
          caixa2.remover()
        print(f'{caixa1.cabeca.nome} foi chamado para o caixa 1')
        caixa1.proximo()
    else:
      if caixa2.tamanho > 0:
        print(f'{caixa2.cabeca.nome} foi chamado para o caixa 2')
        caixa2.proximo()
      else:
        for i in range(caixa1.tamanho - math.ceil(caixa1.tamanho/2)):
          caixa2.inserir(caixa1.final.nome, caixa1.final.valor)
          caixa1.remover()
        print(f'{caixa2.cabeca.nome} foi chamado para o caixa 2')
        caixa2.proximo()
    ''')







