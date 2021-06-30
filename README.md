
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
- **Python 3.8:** É onde se encontra o corpo inteiro da aplicação

- **Computadores com conexão em LAN:** Os computadores que vão se comunicar via rede com o servidor
  
- **Computador:** Espaço interno de 1MB, Processador   

## Porque usamos o Protocolo TCP 

<p>Em linhas bem gerais - o protocolo TCP divide a informação a ser transmitida em pacotes. Esses pacotes são enviados ao destino e, caso algum deles não chegue, ou chegue corrompido, o destino pode solicitar por esses pacotes de novo. Graças ao cabeçalho que o protocolo define em cima de cada pacote, o cliente consegue determinar se algum deles está faltando ou não. Já o protocolo UDP também quebra a informação em pacotes menores mas não tem o cuidado com a integridade ou a correção de perdas. Em vista disso optamos por escolher o TCP, pois a aplicação necessita de uma integridade de dados para que não haja erros no programa, visto que ao movimentar peças as informações não podem ser comprometidas ou perdidas.
</p>
  
### Conexão a partir do cliente

```sh
import socket

class ConexaoCliente:

  def __init__(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    enderecoServidor = ('10.0.0.106', 5000)
    self.sock.connect(enderecoServidor)


  def enviar(self, dado):
    self.sock.sendall(dado.encode('utf-8'))


  def receber(self):
    dado = self.sock.recv(1024)

    # if not dado:
      # Conexão perdida com o cliente

    return dado.decode('utf-8')


  def finalizar(self):
    self.sock.close()
```
  
### Conexão a partir do servidor

```sh
import socket

class ConexaoServidor:

  def __init__(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    enderecoServidor = ('10.0.0.106', 5000)
    sock.bind(enderecoServidor)
    sock.listen(1)
    self.conexao, self.enderecoCliente = sock.accept()

  def enviar(self, dado):
    self.conexao.sendall(dado.encode('utf-8'))

  def receber(self):
    dado = self.conexao.recv(1024)

    # if not dado:
      # Conexão perdida com o cliente

    return dado.decode('utf-8')
```
  


</body>
</html>


