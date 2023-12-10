import socket
import select
Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
adr, port = "127.0.0.9", 123
Server.bind((adr, port))
Server.listen(4)


Conn_client = True
socket_objs = [Server]

while Conn_client:
    list_lue, list_acc_ecrit, exception = select.select(socket_objs, [], socket_objs)
    for socket_obj in list_lue:
        if socket_obj is Server:
            client, adresse = Server.accept()
            socket_objs.append(client)
        else:
            donnees_recue = socket_obj.recv(128).decode("utf-8")
            if donnees_recue:
                print(donnees_recue)
            else:
                socket_objs.remove(socket_obj)
                print("1 participant est déconnecté")
                print(f"{len(socket_objs)-1}participants restants")
