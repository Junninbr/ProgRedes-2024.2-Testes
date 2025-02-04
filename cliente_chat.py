import socket
import threading

host = '127.0.0.1'
porta = 8080

tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSock.connect((host, porta))

def enviar_mensagem():
    while True:
        mensagem = input("Digite sua mensagem: ")
        tcpSock.sendall(mensagem.encode('utf-8'))
        print(f"Enviado: {mensagem}")

def receber_mensagem():
    while True:
        try:
            msg_recebida = tcpSock.recv(1024)
            if not msg_recebida:
                break
            mensagem =  msg_recebida.decode("utf-8")
            print(f"Recebido: {mensagem}")
            
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break

thread_enviarMsg = threading.Thread(target=enviar_mensagem) # Threads das funções
thread_receberMsg = threading.Thread(target=receber_mensagem)

print(f"Conectado em: {host, porta}")

thread_enviarMsg.start()
thread_receberMsg.start()
        

