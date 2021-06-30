import socket
import sys

class Conexao:
    def __init__(self, modo, ip = '', porta = ''):
        self.ip = ip
        self.porta = int(porta)
        self.enderecoServidor = (self.ip, self.porta)
        self.conexao = None
        self.enderecoCliente = None
        self.sock = None

        if(modo == 'servidor'):
            self.IniciarConexaoServidor()
        elif(modo == 'cliente'):
            self.IniciarConexaoCliente()
    
    def IniciarConexaoServidor(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.enderecoServidor)
        self.sock.listen(1)
        self.conexao, self.enderecoCliente = self.sock.accept()

    def EnviarServidor(self, dado):
        self.conexao.sendall(dado.encode('utf-8'))

    def ReceberServidor(self):
        dado = self.conexao.recv(1024)

        if(not dado):
            print('Conexão com cliente perdida.')
            sys.exit(1)

        return dado.decode('utf-8')

    def IniciarConexaoCliente(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        i = 0
        while(True):
            try:
                self.sock.connect(self.enderecoServidor)
                break
            except:
                print('Conexão recusada. Tentando novamente...')

                i += 1

                if(i == 5):
                    print('Conexão falhou! Cheque as informações de IP e porta, depois tente novamente.')
                    sys.exit(1)

    def EnviarCliente(self, dado):
        self.sock.sendall(dado.encode('utf-8'))

    def ReceberCliente(self):
        dado = self.sock.recv(1024)

        if(not dado):
            print('Conexão com servidor perdida.')
            sys.exit(1)

        return dado.decode('utf-8')

    def Finalizar(self):
        self.sock.close()