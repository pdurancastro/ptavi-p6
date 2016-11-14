#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
SERVER = 'localhost'
METODO = sys.argv[1]
DIRECCION = sys.argv[2]
ListaInfo = DIRECCION.split(':')
print(ListaInfo)
PORT = int(ListaInfo[1])
#SERVER = ListaInfo[0]
#print(SERVER)

if len(sys.argv) != 3:
    print("Usage: python client.py method receiver@IP:SIPport")
    sys.exit()



# Contenido que vamos a enviar
LINE = METODO + " " + SERVER+ " " + str(PORT)

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

#print('Recibido --\r\n', data.decode('utf-8'))
print(data.decode('utf-8'))

#Analizaria si tengo un 200 OK y mandaria de nuevo un ACK en este punto
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
