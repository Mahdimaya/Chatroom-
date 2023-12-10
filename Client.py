import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adr, port = "127.0.0.9", 123
client.connect((adr, port))

Nom = input('Donnez votre nom')

if __name__ == '__main__':
    while True:
        message = input(f"{Nom}>")
        client.send(f"{Nom} > {message}".encode("utf-8"))
