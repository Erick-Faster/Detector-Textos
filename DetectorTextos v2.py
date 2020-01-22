# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 03:34:52 2019

Um texto eh introduzido em texto[]
Palavras novas serao inseridas em analise[]
Palavras conhecidas em dicionario[]

@author: Faster-PC
"""
import shelve, os

#Realiza a busca pela palavra no dicionario
def busca(texto,i, dicionario):
    
    #Percorre o dicionario
    for j in range(len(dicionario)):
        if texto[i] == dicionario[j]:
            return "encontrado"
    return texto[i]

#Analisa todo o texto comparando com o dicionario
def analiseTexto(texto, dic):
    analise = []
    
    #Percorre o texto
    for i in range(len(texto)):
        palavra = busca(texto, i, dic)
        if palavra != "encontrado": #Caso nao encontre a palavra
            analise.append(palavra)
    return analise

#Pede para adicionar um texto, para quebrar em uma lista
def capturaTexto():
    texto = input("Adicione o texto\n>>");
    texto = texto.lower() #Coloca tudo em minusculo

    #Remove elementos estranhos
    elementos = "/()[]{}!?@#$%+:;,.=*\"\'\\º°ª" #elementos eliminados
    for i in range(len(elementos)):
        texto =texto.replace(elementos[i],"") #substitui elemento para vazio no texto
    
    texto = texto.split() #Quebra palavras para listas
    return texto

#Le arquivo Shelf
def dicRead(idioma):
    if (os.path.isfile('./Dicionario.bak')): #Caso ja exista dicionario
        shelfFile = shelve.open('Dicionario')
        dic = shelfFile[idioma]
        shelfFile.close()
    else: #Caso nao exista dicionario
        dic = []
        dicWrite(dic, idioma)
    return dic
        
#Escreve arquivo shelf
def dicWrite(dic, idioma):
    shelfFile = shelve.open('Dicionario')
    shelfFile[idioma] = dic
    shelfFile.close()

#Solicita para atualizar o dicionario
def salvarTexto(dic, analise):   
    opcao = input("Deseja atualizar o dicionario? [1]Sim [2]Nao")
    if opcao == '1':
        for i in range (len(analise)):
            dic.append(analise[i])
        dicWrite(dic, idioma)

#Imprime as palavras novas em linha
def imprimePalavras(analise):
    print("Palavras novas Encontradas:")
    for i in range(len(analise)):
        print("-> %s"%analise[i])

'''
MAIN
'''

idioma = input("Em qual idioma voce quer salvar?")

dicionario = dicRead(idioma) #Le as palavras do dicionario
texto = capturaTexto() #le texto introduzido pelo usuario
analise = analiseTexto(texto, dicionario) #Compara palavras do texto com dicionario

imprimePalavras(analise) #Imprime as palavras novas encontradas
salvarTexto(dicionario,analise) #Solicita salvar palavras novas no dicionario


