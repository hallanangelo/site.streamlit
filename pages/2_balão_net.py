import streamlit as st 

st.set_page_config(page_title="Balão Net")
st.title('Balão Net')
st.code('''class No:
    def __init__(self, anterior, valor, proximo):
        self.anterior = anterior
        self.valor = valor
        self.proximo = proximo
        

class duplamenteEncadeada:
    def __init__(self):
        self.cabeca = None 
        self.final = None 
        self.tamanho = 0 
        
    def adicionar(self, valor):
        if self.cabeca == None:
            self.cabeca = No(None, valor, None)
            self.tamanho += 1 
        else:
            ponteiro = self.cabeca
            while ponteiro.proximo:
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(ponteiro, valor, None)
            self.final = ponteiro.proximo
            self.tamanho += 1 
   
    def exibir(self):
        ponteiro = self.final 
        print(ponteiro.valor)
        while ponteiro.anterior:
          ponteiro = ponteiro.anterior
          print(ponteiro.valor)

    def remover(self, valor):
        ponteiro = self.cabeca 
        while ponteiro.valor != valor:
            ponteiro = ponteiro.proximo
        if ponteiro.proximo and ponteiro.anterior:
            ponteiro.anterior.proximo = ponteiro.proximo
            ponteiro.proximo.anterior = ponteiro.anterior
        else: 
            if ponteiro.proximo:
                self.cabeca = ponteiro.proximo 
                ponteiro.proximo.anterior = None 
            else:
                ponteiro.anterior.proximo = None 
                self.final = ponteiro.anterior
        self.tamanho -= 1

    def procurar(self, valor):
      ponteiro = self.cabeca
      while ponteiro.valor != valor:
          ponteiro = ponteiro.proximo 
      if ponteiro == self.final:
          pass
      elif ponteiro == self.cabeca:
          self.cabeca = ponteiro.proximo
          self.cabeca.anterior = None
      else:  
          ponteiro.anterior.proximo = ponteiro.proximo
          ponteiro.proximo.anterior = ponteiro.anterior
      self.final.proximo = ponteiro
      ponteiro.anterior = self.final
      self.final = ponteiro
      ponteiro.proximo = None    
    

lista = duplamenteEncadeada()

fim_de_loop = False
while fim_de_loop == False :

    comando = input().split(' ')
    
    if comando[0]=='ADD':
        lista.adicionar(comando[1])
    
    elif comando[0]=='REM':
        lista.remover(comando[1])

    elif comando[0]=='FIND':
        lista.procurar(comando[1])

    elif comando[0]=='EXIB':
        lista.exibir()

    else:
        fim_de_loop = True
  



''')
    