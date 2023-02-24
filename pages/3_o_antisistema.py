import streamlit as st 

st.set_page_config(page_title="O antisistema")
st.title('O Antisistema')
st.code('''def pilhalmaculada(pilha):
    for i in range(len(pilha)):
        if (i + 1) == len(pilha):
            return "Está tudo certo"
        elif int(pilha[i]) > int(pilha[i + 1]):
            return "A pilha está um caos."

def novaLocacao(pilha, codigo):
  for i in range(len(pilha)):
    if codigo < int(pilha[i]):
      pilha.insert(i, str(codigo))
      return pilha


pilha = input().split(',')
resultado = pilhalmaculada(pilha)
if resultado == 'A pilha está um caos.':
  print(resultado)
else: 
  print(novaLocacao(pilha, int(input())))
''')