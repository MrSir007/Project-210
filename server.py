import socket
from threading import Thread

SERVER = None
ip_address = "127.0.0.1"
port = 1050
buffer_size = 4096
clients = {}

def acceptConnections () :
  global SERVER
  global clients

  while True :
    client, addr = SERVER.accept()
    client_name = client.recv(4096).decode().lower()
    clients[client_name]  = {
      "client": client,
      "address": addr,
      "connected_with": "",
      "file_name": "",
      "file_size": 4096
    }

    print(f"Connection established with {client_name} : {addr}")

    thread = Thread(target=handleClient, args=(client, client_name,))
    thread.start()

    

def setup () :
  print("\n\t\t\t\t\tIP Messager\n")

  global SERVER
  global ip_address
  global port

  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.bind((ip_address, port))

  SERVER.listen(100)

  print("\t\t\t\tServer is waiting for incoming connection...")
  print("\n")

  acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()