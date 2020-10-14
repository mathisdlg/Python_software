import socket

condition_arret = False
while condition_arret != True:
    s_or_c = input("Are-you client or server[c-s]: ")
    if s_or_c == "c" or s_or_c == "C":
        condition_arret = True
    else:
        if s_or_c == "s" or s_or_c == "S":
            condition_arret = True

if s_or_c == "s" or s_or_c == "S":
    print("You are the server")

    condition_arret = False

    while condition_arret != True:
        port = int(input("Enter the port for the server[1024-65536]: "))
        if port >= 1024 and port <= 65536:
            condition_arret = True
        else:
            pass

    hote = ""
    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((hote, port))
    connexion_principale.listen(5)
    print("Server listen on port {}".format(port))

    connexion_avec_client, infos_connexion = connexion_principale.accept()

    arret = False
    msg_recu = b""
    while arret != True:
        msg_recu = (connexion_avec_client.recv(1000000000)).decode()
        if msg_recu == "end":
            arret = True
            print("Connexion close.")
            connexion_avec_client.close()
            connexion_principale.close()
        else:
            print(msg_recu)
            msg_send = input(">")
            if msg_send == "end":
                arret = True
                msg_send = msg_send.encode()
                connexion_avec_client.send(msg_send)
                print("Connexion close.")
                connexion_avec_client.close()
            else:
                connexion_avec_client.send(msg_send.encode())



else:
    print("You are the client")

    hote = input("Enter IP address of the sever: ")

    condition_arret = False
    while condition_arret != True:
        port = int(input("Enter the port to connect to the server[1024-65536]: "))
        if port >= 1024 and port <= 65536:
            condition_arret = True
        else:
            pass

    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion enable on port {}".format(port))

    arret = False
    msg_a_envoyer = b""
    while arret != True:
        msg_a_envoyer = input("> ")
        if msg_a_envoyer == "end":
            arret = True
            msg_a_envoyer = msg_a_envoyer.encode()
            connexion_avec_serveur.send(msg_a_envoyer)
            print("Connexion close.")
            connexion_avec_serveur.close()
        else:
            msg_a_envoyer = msg_a_envoyer.encode()
            connexion_avec_serveur.send(msg_a_envoyer)
            msg_recu = (connexion_avec_serveur.recv(1000000000)).decode()
            print(msg_recu)
