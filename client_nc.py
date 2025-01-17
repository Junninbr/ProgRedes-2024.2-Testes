import socket

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

resposta_decode = resposta.decode()
print(resposta_decode)