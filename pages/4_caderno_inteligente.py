import streamlit as st 

st.set_page_config(page_title="Caderno Inteligente")
st.title('Caderno Inteligente')
st.code('''pilha = list(input())
booleano = 0
quantidade = 0
verificador = True
posicao = []

#pilha: recebe a entrada e separa a entrada em uma lista
#booleano: avalia a quantidade de V e F 
#quantidade: verifica a quantidade de letras que já foram conferidas
#verificador: mantém o laço de repetição ativo
#posicao: adiciona a posicao dos F que ainda precisam do V 


while verificador:
  if quantidade == len(pilha): #Caso todos os booleanos sejam conferidos, o condicional avaliará se a regra foi seguida.
    if booleano > 0:
      print(f"Incorreto, devido a capa na posição {posicao[0]}.")
    else:
      print("Correto.")
    verificador = False
  elif pilha[quantidade] == 'F':
    booleano += 1
    posicao.append(str(quantidade + 1))
  elif pilha[quantidade] == 'V':
    if len(posicao) == 0:
      verificador = False
      print(f"Incorreto, devido a capa na posição {quantidade + 1}.")
    else:
      del posicao[0]
      booleano -= 1
  quantidade += 1
  


''')