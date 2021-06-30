<html>
<body>
  
<h5>
  Discentes: Breno Moreira, Daniel Penedo, Jenilson Ramos e Nassim Rihan <br>
  Docente: Jorge Lima <br>
  Disciplina: Redes I <br>
</h5>
<h2 align="center"> Projeto Cliente-Servidor em Python </h2>
  
## Introdução
<p>Apresentaremos uma implementação de um jogo de xadrez que conecta cliente-servidor para que dois jogadores possam jogar um contra o outro via Rede. O intuito deste projeto é mostrar a conexão para que duas máquinas consigam se comunicar através de um programa cliente e um programa servidor.
</p>
  
<p>Usamos um protocolo TCP que servem para quebrar em partes menos e enviar o arquivo pro endereço correto onde haverá a comunicação entre cliente e servidor, e a linguagem de programação Python v3.8, com adição do módulo de interface gráfica GTK e a biblioteca "socket", para nos auxiliar neste projeto. 
</p>  

## Requisitos Mínimos
- **Python 3.8:** É onde se encontra o corpo inteiro da aplicação;

- **Computadores com conexão em LAN:** Os computadores que vão se comunicar via rede com o servidor;
  
- **Computador:** 2GB de RAM, Processador Celeron.  

## Porque usamos o Protocolo TCP 

<p>Em linhas bem gerais - o protocolo TCP divide a informação a ser transmitida em pacotes. Esses pacotes são enviados ao destino e, caso algum deles não chegue, ou chegue corrompido, o destino pode solicitar por esses pacotes de novo. Graças ao cabeçalho que o protocolo define em cima de cada pacote, o cliente consegue determinar se algum deles está faltando ou não. Já o protocolo UDP também quebra a informação em pacotes menores mas não tem o cuidado com a integridade ou a correção de perdas. Em vista disso optamos por escolher o TCP, pois a aplicação necessita de uma integridade de dados para que não haja erros no programa, visto que ao movimentar peças as informações não podem ser comprometidas ou perdidas.
</p>
  
## Camada de Aplicação 

 - **Protocolo de aplicação:** A conexão se inicia pela máquina HOST ou SERVIDOR. 
 - **Sockets:** Dois programas executados na mesma máquina ou dois computadores distintos podem se comunicar via uma série de funcionalidades de linguagem de programação e uma delas são os sockets.  Fazem a “ligação” do SO, que implementa os protocolos de transporte, rede, ... com aplicações que estão sendo executadas.
- **Informações de nível de rede:** Endereço.
- **Informações de nível de transporte:**
      <br>– Protocolo;
      <br>– Porta.
  
### Conexão servidor/cliente

```sh
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
        self.sock.close()```
```
### Funcionamento do Software 
<p>Inicializamos a aplicação criando um socket para fazer a ligação, logo após críamos um métodos para leitura dos dados de IP e Porta para que possamos dar entrada na conexão e testar se o socket já está "ouvindo".</p> 
<p> Temos uma constante própria que especifica a comunicação remota, chamada de AF_INET. Essa constante faz parte de um grupo denominado famílias de endereços, ou address families, que constitui exatamente o primeiro parâmetro opcional do construtor socket. A AF_INET abrange os endereços do tipo IPv4, antigo padrão da Internet.</p>
<p>Em relação ao tipo do socket, existem duas constantes mais importantes - a SOCK_STREAM, que define sockets de fluxo, e a SOCK_DGRAM, que define sockets de datagrama. Estamos usando a SOCK_STREAM pois basicamente, um socket de fluxo se refere ao protocolo TCP, enquanto um socket de datagrama, ao UDP.</p>
<p> Temos também métodos responsáveis por controlar o envio e o recebimento das mensagens, o tipo de dado é uma string codificada em UTF-8 que contém as posições das peças de xadrez.</p>
  
- **Bind():** Associa o soquete ao seu endereço local [é por isso que o lado do servidor se liga, para que os clientes possam usar esse endereço para se conectar ao servidor.]; 
- **Connect():** É usado para se conectar a um endereço [servidor] remoto, é por isso que é do lado do cliente , conectar [ler como: conectar ao servidor] é usado;
- **Listen():** É responsável por permitir que o servidor aceite conexões;
- **Accept():** É responsável por aceitar a conexão; 
  
</body>
</html>
