from random import randint
import os

palavras = ['carro', 'farol', 'bola', 'brasil', 'internet', 'arvore', 'python', 'abacaxi', 'manga', 'piscina', 'cerveja', 'pagode', 'laranja', 'tapioca', 'peixe', 'cuscuz', 'lagarto', 'mortadela', 'dorsal', 'infinity', 'dinheiro', 'lula']
nomeJogador = input('Qual o seu nome, jogador(a)? ')
palavra = palavras[randint(0, len(palavras) - 1)].upper()
lacuna = '_'
erros = 0
palavraIncompleta = list(len(palavra) *lacuna)

def mensagem(): 
    os.system('cls')
    print('\033[1m//////// JOGO DA FORCA ////////\033[0m')
    print(f'\x1B[3mOlá, {nomeJogador}! O jogo consiste em acertar a palavra oculta informando uma letra por vez.')
    print('Cuidado, com 6 erros você perderá o desafio.\x1B[0m\n')
    print(f'\033[93mPalavra de {len(palavra)} letras: {" ".join(palavraIncompleta).upper()}\033[0m')

def letra(l):
    for i in range(len(palavra)):
        if l == palavra[i]: 
            palavraIncompleta[i] = l
    mensagem()

def checagem(chute):
    global erros
    if len(chute) > 1: 
        print('Digite apenas 1 letra por vez.')
        return
    if type(chute) == int:
        print(f'Apenas letras, {nomeJogador}.')
        return
    if erros < 6:
        if chute in palavra:
            letra(chute)
        else:
            erros = erros + 1
            print(f'Não tem "{chute}" na palavra. \033[94mErros: {erros}\033[0m')
    else: 
        erros = erros + 1
        print(f'Que pena! Você errou 6 vezes. A palavra era "{palavra}".')

mensagem()
chute = input('Escolha uma letra: ').upper()
checagem(chute)

while "".join(palavraIncompleta) != palavra and erros < 6: 
    chute = input('Escolha uma letra: ').upper()
    checagem(chute)

else: 
    if "".join(palavraIncompleta) == palavra: print(f'\033[1m\033[92mParabéns, {nomeJogador}!\033[0m')
    else: print('\033[91mVocê matou o bonequinho :(\033[0m')
