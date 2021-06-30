import socket

class Conexao:
    def __init__(self, modo, ip = '', porta = ''):
        self.ip = ip
        self.porta = porta

        if(modo == 'servidor'):
            self.IniciarConexaoServidor()
        elif(modo == 'cliente'):
            self.IniciarConexaoCliente()
    
    def IniciarConexaoServidor(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.enderecoServidor = (self.ip, self.porta)
        self.sock.bind(self.enderecoServidor)
        self.sock.listen(1)
        self.conexao, self.enderecoCliente = self.sock.accept()

    def EnviarServidor(self, dado):
        self.conexao.sendall(dado.encode('utf-8'))

    def ReceberServidor(self):
        dado = self.conexao.recv(1024)

        # if not dado:
        # Conexão perdida com o cliente

        return dado.decode('utf-8')

    def IniciarConexaoCliente(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.enderecoServidor = (self.ip, self.porta)
        self.sock.connect(self.enderecoServidor)

    def EnviarCliente(self, dado):
        self.sock.sendall(dado.encode('utf-8'))

    def ReceberCliente(self):
        dado = self.sock.recv(1024)

        # if not dado:
        # Conexão perdida com o cliente

        return dado.decode('utf-8')

    def FinalizarCliente(self):
        self.sock.close()