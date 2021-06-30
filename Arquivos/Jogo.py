import time
import os
import sys
from random import randint
from Arquivos.Usuario import Usuario
from Arquivos.Conexao import Conexao
from Arquivos.Pecas import *


class ConjuntoPecas:
    def __init__(self, corPecas, corUsuario):
        self.cor = corPecas

        self.pecas = []

        if(corUsuario == 'Brancas'):
            if(self.cor == 'Pretas'):
                i = 0
                while i < 8:
                    self.pecas.append(Peao([1, i], False, True))
                    i += 1

                self.pecas.append(Torre([0, 0], False))
                self.pecas.append(Cavalo([0, 1], False))
                self.pecas.append(Bispo([0, 2], False))
                self.pecas.append(Dama([0, 3], False))
                self.pecas.append(Rei([0, 4], False))
                self.pecas.append(Bispo([0, 5], False))
                self.pecas.append(Cavalo([0, 6], False))
                self.pecas.append(Torre([0, 7], False))
                

            elif(self.cor == 'Brancas'):
                i = 0
                while i < 8:
                    self.pecas.append(Peao([6, i], True, True))
                    i += 1
                
                self.pecas.append(Torre([7, 0], True))
                self.pecas.append(Cavalo([7, 1], True))
                self.pecas.append(Bispo([7, 2], True))
                self.pecas.append(Dama([7, 3], True))
                self.pecas.append(Rei([7, 4], True))
                self.pecas.append(Bispo([7, 5], True))
                self.pecas.append(Cavalo([7, 6], True))
                self.pecas.append(Torre([7, 7], True))


        elif(corUsuario == 'Pretas'):
            if(self.cor == 'Brancas'):
                i = 0
                while i < 8:
                    self.pecas.append(Peao([1, i], True, False))
                    i += 1

                self.pecas.append(Torre([0, 0], True))
                self.pecas.append(Cavalo([0, 1], True))
                self.pecas.append(Bispo([0, 2], True))
                self.pecas.append(Dama([0, 3], True))
                self.pecas.append(Rei([0, 4], True))
                self.pecas.append(Bispo([0, 5], True))
                self.pecas.append(Cavalo([0, 6], True))
                self.pecas.append(Torre([0, 7], True))


            if(self.cor == 'Pretas'):
                i = 0
                while i < 8:
                    self.pecas.append(Peao([6, i], False, False))
                    i += 1

                self.pecas.append(Torre([7, 0], False))
                self.pecas.append(Cavalo([7, 1], False))
                self.pecas.append(Bispo([7, 2], False))
                self.pecas.append(Dama([7, 3], False))
                self.pecas.append(Rei([7, 4], False))
                self.pecas.append(Bispo([7, 5], False))
                self.pecas.append(Cavalo([7, 6], False))
                self.pecas.append(Torre([7, 7], False))


    def EstaCheck(self, tabuleiro, outroConjunto):
        for p in outroConjunto.pecas:
            posicao = p.posicao
            if(posicao[0] > 0 and posicao[1] > 0):
                if(p.verificaMovimento(self.pecas[12], tabuleiro)):
                    return(True)

        return(False)

    def EstaCheckmate(self, tabuleiro, outroConjunto):
        posicaoRei = self.pecas[12].posicao
        x = posicaoRei[0]
        y = posicaoRei[1]

        posiveisCasas = [[x-1,y], [x+1, y], [x, y-1], [x, y+1], [x-1, y-1], [x+1, y+1], [x-1, y+1], [x+1, y-1]]

        casasPermitidas = []
        for c in posiveisCasas:
            peca = Peca(c)
            if(self.pecas[12].verificaMovimento(peca, tabuleiro)):
                casasPermitidas.append(peca)

        casasNaoPermitidas = casasPermitidas[:]
        for p in outroConjunto.pecas:
            for i, c in enumerate(casasPermitidas):
                if(p.verificaMovimento(c, tabuleiro)):
                    casasNaoPermitidas[i] = None

        for x in casasNaoPermitidas:
            if(x != None):
                return(False)

        return(True)


def PrepararTabuleiro(usuario, ConjuntoPecasBrancas, ConjuntoPecasPretas):

    tabuleiro = []

    for x in range(8):
        tabuleiro.append([])
        for y in range(8):
            tabuleiro[x].append(Peca([x, y]))
        
    if(usuario.corPecas == 'Brancas'):
        # Peças Pretas
        # Linha do Rei
        tabuleiro[0][0] = ConjuntoPecasPretas.pecas[8]
        tabuleiro[0][1] = ConjuntoPecasPretas.pecas[9]
        tabuleiro[0][2] = ConjuntoPecasPretas.pecas[10]
        tabuleiro[0][3] = ConjuntoPecasPretas.pecas[11]
        tabuleiro[0][4] = ConjuntoPecasPretas.pecas[12]
        tabuleiro[0][5] = ConjuntoPecasPretas.pecas[13]
        tabuleiro[0][6] = ConjuntoPecasPretas.pecas[14]
        tabuleiro[0][7] = ConjuntoPecasPretas.pecas[15]
        
        # Linha dos peões
        i = 0
        while i < 8:
            tabuleiro[1][i] = ConjuntoPecasPretas.pecas[i]
            i += 1

        
        # Peças Brancas
        # Linha dos peões
        i = 0
        while i < 8:
            tabuleiro[6][i] = ConjuntoPecasBrancas.pecas[i]
            i += 1
        
        # Linha do Rei
        tabuleiro[7][0] = ConjuntoPecasBrancas.pecas[8]
        tabuleiro[7][1] = ConjuntoPecasBrancas.pecas[9]
        tabuleiro[7][2] = ConjuntoPecasBrancas.pecas[10]
        tabuleiro[7][3] = ConjuntoPecasBrancas.pecas[11]
        tabuleiro[7][4] = ConjuntoPecasBrancas.pecas[12]
        tabuleiro[7][5] = ConjuntoPecasBrancas.pecas[13]
        tabuleiro[7][6] = ConjuntoPecasBrancas.pecas[14]
        tabuleiro[7][7] = ConjuntoPecasBrancas.pecas[15]

    elif(usuario.corPecas == 'Pretas'):
        # Peças Brancas
        # Linha do Rei
        tabuleiro[0][0] = ConjuntoPecasBrancas.pecas[8]
        tabuleiro[0][1] = ConjuntoPecasBrancas.pecas[9]
        tabuleiro[0][2] = ConjuntoPecasBrancas.pecas[10]
        tabuleiro[0][3] = ConjuntoPecasBrancas.pecas[11]
        tabuleiro[0][4] = ConjuntoPecasBrancas.pecas[12]
        tabuleiro[0][5] = ConjuntoPecasBrancas.pecas[13]
        tabuleiro[0][6] = ConjuntoPecasBrancas.pecas[14]
        tabuleiro[0][7] = ConjuntoPecasBrancas.pecas[15]

        # Linha dos peões
        i = 0
        while i < 8:
            tabuleiro[1][i] = ConjuntoPecasBrancas.pecas[i]
            i += 1


        # Peças Pretas
        # Linha dos peões
        i = 0
        while i < 8:
            tabuleiro[6][i] = ConjuntoPecasPretas.pecas[i]
            i += 1

        # Linha do Rei
        tabuleiro[7][0] = ConjuntoPecasPretas.pecas[8]
        tabuleiro[7][1] = ConjuntoPecasPretas.pecas[9]
        tabuleiro[7][2] = ConjuntoPecasPretas.pecas[10]
        tabuleiro[7][3] = ConjuntoPecasPretas.pecas[11]
        tabuleiro[7][4] = ConjuntoPecasPretas.pecas[12]
        tabuleiro[7][5] = ConjuntoPecasPretas.pecas[13]
        tabuleiro[7][6] = ConjuntoPecasPretas.pecas[14]
        tabuleiro[7][7] = ConjuntoPecasPretas.pecas[15]

    return(tabuleiro)


def ImprimirTabuleiro(tabuleiro):
    os.system('clear || cls')

    print()
    print('### XADREZ ###')
    print()

    print('  ', end='')
    for x in range(8):
        auxStr = ' ' + str(x) + ' '
        print(auxStr, end='')
    print()

    for i, x in enumerate(tabuleiro):
        print(str(i) + ' ', end='')
        for y in x:
            print(y.pecaChar, end='')
        print()

    print()
    print()


def MoverPecas(tabuleiro, origem, destino):
    pecaOrigem = tabuleiro[origem[0]][origem[1]]
    pecaDestino = tabuleiro[destino[0]][destino[1]]

    if(pecaOrigem.cor == pecaDestino.cor):
        return(False, tabuleiro)
    elif(pecaOrigem.verificaMovimento(pecaDestino, tabuleiro)):
        pecaOrigem.posicao = destino

        pecaDestino = pecaOrigem

        pecaOrigem = Peca([origem[0], origem[1]])

        tabuleiro[origem[0]][origem[1]] = pecaOrigem
        tabuleiro[destino[0]][destino[1]] = pecaDestino

        return(True, tabuleiro)

    return(False, tabuleiro)


def EscolherCorServidor(conexao):
    tempoInicioEscolha = time.time()

    corEscolhidaLocal = input('Escolha a cor (b/p): ')

    tempoFimEscolha = time.time()

    tempoDemoraSegundosLocal = float('{:.5f}'.format(tempoFimEscolha - tempoInicioEscolha))
    
    print('Aguardando escolha do cliente...\n')
    dadoRecebido = conexao.ReceberServidor()
    dadoRecebido = dadoRecebido.split(';')
    corEscolhidaLan = dadoRecebido[0]
    tempoDemoraSegundosLan = float(dadoRecebido[1])

    corEscolhidaLocal = 'Brancas' if corEscolhidaLocal == 'b' else 'Pretas'
    corEscolhidaLan = 'Brancas' if corEscolhidaLan == 'b' else 'Pretas'

    if(corEscolhidaLocal == corEscolhidaLan):
        if(tempoDemoraSegundosLocal < tempoDemoraSegundosLan):
            corEscolhidaLan = 'Brancas' if corEscolhidaLocal == 'Pretas' else 'Pretas'
        elif(tempoDemoraSegundosLocal > tempoDemoraSegundosLan):
            corEscolhidaLocal = 'Brancas' if corEscolhidaLan == 'Pretas' else 'Pretas'
        else:
            cores = ['Brancas', 'Pretas']

            i = randint(0, 1)

            corEscolhidaLocal = cores[i]

            i = 0 if i == 1 else 1

            corEscolhidaLan = cores[i]

    dadoEnvio = corEscolhidaLan
    conexao.EnviarServidor(dadoEnvio)

    return(corEscolhidaLocal)

def EscolherCorCliente(conexao):
    tempoInicioEscolha = time.time()

    corEscolhidaLocal = input('Escolha a cor (b/p): ')

    tempoFimEscolha = time.time()

    tempoDemoraSegundosLocal = tempoFimEscolha - tempoInicioEscolha

    #Cor;tempoDemoraSegundosLocal
    dadoEnvio = corEscolhidaLocal + ';' + '{:.5f}'.format(tempoDemoraSegundosLocal)

    conexao.EnviarCliente(dadoEnvio)
    
    print('Aguardando escolha do servidor...\n')
    corEscolhidaLocal = conexao.ReceberCliente()

    return(corEscolhidaLocal)


def TratarJogada(jogada):
    try:
        jogada = jogada.split()
        jogada = ''.join(jogada)
        jogada = jogada.split('=>')
        origem = jogada[0].split('x')
        destino = jogada[1].split('x')

        origem[0] = int(origem[0])
        origem[1] = int(origem[1])
        destino[0] = int(destino[0])
        destino[1] = int(destino[1])

        return origem, destino

    except:
        print('Entrada incorreta!\n')
        return False, False


def JogarServidor(tabuleiro, pecasBrancas, pecasPretas, usuario, conexao):
    try:
        numeroTurno = 1
        perdeu = False
        conjuntoAdversario = None
        
        ImprimirTabuleiro(tabuleiro)

        if(usuario.corPecas == 'Brancas'):
            numeroJogador = 1
            numeroAdversario = 2
            conjuntoAdversario = pecasPretas
        elif(usuario.corPecas == 'Pretas'):
            numeroJogador = 2
            numeroAdversario = 1
            conjuntoAdversario = pecasBrancas

        while(True):
            if(numeroTurno % 3 == numeroJogador):
                while(True):
                    print('Está na sua vez.\n')

                    jogada = input()
                    origem, destino = TratarJogada(jogada)

                    if(origem != False and destino != False):
                        break

                (status, tabuleiro) = MoverPecas(tabuleiro, origem, destino)

                if(status):
                    dadoEnvio = jogada
                    conexao.EnviarServidor(dadoEnvio)

                    numeroTurno += 1
                else:
                    input('Jogada irregular!\n')

            elif(numeroTurno % 3 == numeroAdversario):
                print('Está na vez do outro jogador.\n')

                #Esperar Jogada Lan
                jogada = conexao.ReceberServidor()

                origem, destino = TratarJogada(jogada)

                origem[0] = 7 - origem[0]
                origem[1] = 7 - origem[1]
                destino[0] = 7 - destino[0]
                destino[1] = 7 - destino[1]

                (status, tabuleiro) = MoverPecas(tabuleiro, origem, destino)

                numeroTurno += 1

            elif(numeroTurno % 3 == 0):
                dadoEnvio = str(perdeu)

                situacao = conexao.ReceberServidor()
                conexao.EnviarServidor(dadoEnvio)
                if(situacao == 'True' or dadoEnvio == 'True'):
                    break

                numeroTurno += 1

            ImprimirTabuleiro(tabuleiro)

            if(usuario.conjuntoPecas.EstaCheckmate(tabuleiro, conjuntoAdversario)):
                perdeu = True

            if(usuario.conjuntoPecas.EstaCheck(tabuleiro, conjuntoAdversario)):
                print('\033[91m' + 'Você está em check!' + '\033[0m')
                print()
                print()
            

        if(perdeu):
            os.system('clear || cls')
            print('\033[91m' + 'Checkmate!\nVocê Perdeu!' + '\033[0m')
            print()
            print()
        else:
            os.system('clear || cls')
            print('\033[92m' + 'Você Ganhou!' + '\033[0m')
            print()
            print()

        conexao.Finalizar()

    except:
        conexao.Finalizar()


def JogarCliente(tabuleiro, pecasBrancas, pecasPretas, usuario, conexao):
    try:
        numeroTurno = 1
        perdeu = False
        conjuntoAdversario = None
        
        ImprimirTabuleiro(tabuleiro)

        if(usuario.corPecas == 'Brancas'):
            numeroJogador = 1
            numeroAdversario = 2
            conjuntoAdversario = pecasPretas
        elif(usuario.corPecas == 'Pretas'):
            numeroJogador = 2
            numeroAdversario = 1
            conjuntoAdversario = pecasBrancas

        while(True):
            if(numeroTurno % 3 == numeroJogador):
                while(True):
                    print('Está na sua vez.\n')

                    jogada = input()
                    origem, destino = TratarJogada(jogada)

                    if(origem != False and destino != False):
                        break

                (status, tabuleiro) = MoverPecas(tabuleiro, origem, destino)

                if(status):
                    dadoEnvio = jogada
                    conexao.EnviarCliente(dadoEnvio)

                    numeroTurno += 1
                else:
                    input('Jogada irregular!\n')

            elif(numeroTurno % 3 == numeroAdversario):
                print('Está na vez do outro jogador.\n')

                #Esperar Jogada Lan
                jogada = conexao.ReceberCliente()

                origem, destino = TratarJogada(jogada)

                origem[0] = 7 - origem[0]
                origem[1] = 7 - origem[1]
                destino[0] = 7 - destino[0]
                destino[1] = 7 - destino[1]

                (status, tabuleiro) = MoverPecas(tabuleiro, origem, destino)

                numeroTurno += 1

            elif(numeroTurno % 3 == 0):
                dadoEnvio = str(perdeu)

                conexao.EnviarCliente(dadoEnvio)
                situacao = conexao.ReceberCliente()
                if(situacao == 'True' or dadoEnvio == 'True'):
                    break

                numeroTurno += 1

            ImprimirTabuleiro(tabuleiro)

            if(usuario.conjuntoPecas.EstaCheckmate(tabuleiro, conjuntoAdversario)):
                perdeu = True

            if(usuario.conjuntoPecas.EstaCheck(tabuleiro, conjuntoAdversario)):
                print('\033[91m' + 'Você está em check!' + '\033[0m')
                print()
                print()
            

        if(perdeu):
            os.system('clear || cls')
            print('\033[91m' + 'Checkmate!\nVocê Perdeu!' + '\033[0m')
            print()
            print()
        else:
            os.system('clear || cls')
            print('\033[92m' + 'Você Ganhou!' + '\033[0m')
            print()
            print()

        conexao.Finalizar()

    except:
        conexao.Finalizar()


def Main():
    while(True):
        modo = input('Modo (servidor/cliente): ')

        if(modo in ['servidor', 'cliente']):
            break
        
        else:
            print('Entrada incorreta!\n')

    usuario = Usuario()

    ip = input('Ip servidor: ')
    porta = input('Porta: ')

    if(modo == 'cliente'):
        print()
        conexao = Conexao(modo, ip, porta)
        print('Conectado.\n')
        usuario.corPecas = EscolherCorCliente(conexao)
        pecasBrancas = ConjuntoPecas('Brancas', usuario.corPecas)
        pecasPretas = ConjuntoPecas('Pretas', usuario.corPecas)

        if(usuario.corPecas == 'Brancas'):
            usuario.conjuntoPecas = pecasBrancas
        elif(usuario.corPecas == 'Pretas'):
            usuario.conjuntoPecas = pecasPretas

        tabuleiro = PrepararTabuleiro(usuario, pecasBrancas, pecasPretas)
        JogarCliente(tabuleiro, pecasBrancas, pecasPretas, usuario, conexao)

    elif(modo == 'servidor'):
        print()
        conexao = Conexao(modo, ip, porta)
        print('Conectado.\n')
        usuario.corPecas = EscolherCorServidor(conexao)
        pecasBrancas = ConjuntoPecas('Brancas', usuario.corPecas)
        pecasPretas = ConjuntoPecas('Pretas', usuario.corPecas)

        if(usuario.corPecas == 'Brancas'):
            usuario.conjuntoPecas = pecasBrancas
        elif(usuario.corPecas == 'Pretas'):
            usuario.conjuntoPecas = pecasPretas

        tabuleiro = PrepararTabuleiro(usuario, pecasBrancas, pecasPretas)
        JogarServidor(tabuleiro, pecasBrancas, pecasPretas, usuario, conexao)