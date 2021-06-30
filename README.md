
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
  
<p>Usamos um protocolo TCP que servem para quebrar em partes menos e enviar o arquivo pro endereço correto onde haverá a comunicação entre cliente e servidor, e a linguagem de programação Python v3.8.0, com adição do módulo de interface gráfica GTK e a biblioteca "socket", para nos auxiliar neste projeto. 
</p>  
  
- **One Dependency:** There is only one build dependency. It uses webpack, Babel, ESLint, and other amazing projects, but provides a cohesive curated experience on top of them.

- **No Configuration Required:** You don't need to configure anything. A reasonably good configuration of both development and production builds is handled for you so you can focus on writing code.

- **No Lock-In:** You can “eject” to a custom setup at any time. Run a single command, and all the configuration and build dependencies will be moved directly into your project, so you can pick up right where you left off.

## Protocolo TCP 

<p>Em linhas bem gerais - o protocolo TCP divide a informação a ser transmitida em pacotes. Esses pacotes são enviados ao destino e, caso algum deles não chegue, ou chegue corrompido, o destino pode solicitar por esses pacotes de novo. Graças ao cabeçalho que o protocolo define em cima de cada pacote, o cliente consegue determinar se algum deles está faltando ou não. Já o protocolo UDP também quebra a informação em pacotes menores mas não tem o cuidado com a integridade ou a correção de perdas. Em vista disso optamos por escolher o TCP, pois a aplicação necessita de uma integridade de dados para que não haja erros no programa, visto que ao movimentar peças as informações não podem ser comprometidas ou perdidas.
</p>
  
### Conexão a partir do cliente

```sh
1 import socket
2 HOST = '127.0.0.1'     # Endereco IP do Servidor
3 PORT = 5000            # Porta que o Servidor esta
4 tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
5 dest = (HOST, PORT)
6 tcp.connect(dest)
```
  
### Conexão a partir do servidor

```sh
1 import socket
2 HOST = ' '     # Endereco IP do Servidor
3 PORT = 5000            # Porta que o Servidor esta
4 tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
5 dest = (HOST, PORT)
6 tcp.connect(dest)
```
  


</body>
</html>


