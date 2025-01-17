import socket
import os

entrada = input("Insira a requisição: ")
host = input("Insira o host e porta: ")
print(host)
site, porta = host.split()

tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSock.connect((site, int(porta)))

request = f"{entrada}\r\n"
request += f"Host: {site}\r\n"
request += "Connection: close\r\n"
request += "\r\n"

tcpSock.sendall(request.encode())


resposta = b""
while True:
    data = tcpSock.recv(4096)  # Recebe em blocos de 4KB
    if not data:
        break
    resposta += data

tcpSock.close()

content = b"Content-Length:"
content_local = resposta.find(content)
print(content_local)

if content_local == 79:
    with open("teste.png", "wb") as f:
        resposta
        
elif content_local == -1:
    header, dados, outros = resposta.split(b"\r\n\r\n")

    print(f"cabeçalho: {header}")
    print(f"dados: {dados}")
    print(f"outros: {outros}")

