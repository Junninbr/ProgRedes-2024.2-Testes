import socket, sys, ssl

def wrapSocket(sock, serverurl):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose)
    return context.wrap_socket(sock, server_hostname=serverurl)


if len(sys.argv) == 4 and sys.argv[2] == "-o":
    hostParts = sys.argv[1].split("://")
    if not hostParts[0] in ["http", "https"]:
        sys.exit(1)

    barIndex = hostParts[1].find("/")
    HOST = hostParts[1][:barIndex]
    resource = hostParts[1][barIndex:]


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if hostParts[0] == "https":
        sock = wrapSocket(sock, HOST)
        PORT = 443
    else:
        PORT = 80

    sock.connect((HOST, PORT))

    req = ('GET '+resource+' HTTP/1.1\r\n'+
           'Host: '+HOST+'\r\n'+
           '\r\n').encode()

    sock.sendall(req)

    resp = sock.recv(4096)
    while b'\r\n\r\n' not in resp:
        resp += sock.recv(4096)

    data = resp.split(b'\r\n\r\n')
    headers = data[0]
    body = data[1]

    headers = headers.split(b'\r\n')
    statusLine = headers[0]
    headers = headers[1:]

    #print (statusLine)
    #print (headers)
    #print(body)

    toRead = 0
    for header in headers:
        header = header.split(b':')
        if header[0] == b'Content-Length':
            toRead = int(header[1])

            if toRead > 0:
                while len(body) < toRead:
                    body += sock.recv(4096)

                fd = open (sys.argv[3], 'wb')
                fd.write(body)
                fd.close()

    if b'Transfer-Encoding: chunked' in headers:
        with open(sys.argv[3], 'wb') as fd:
            while True:
                print(body)
                chunkData = body.split(b"\r\n")
                bytesHex = chunkData[0]
                toRead = int(bytesHex, 16)  
                dadosChunk = b""
                if toRead == 0:
                    break  
                else:
                    
                    dadosChunk = chunkData[1]
                    fd.write(dadosChunk)
                    

            
    sock.close()