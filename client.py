#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
METODO = sys.argv[1]
DIRECCION = sys.argv[2]
ListaInfo = DIRECCION.split(':')
# print(ListaInfo)
PORT = int(ListaInfo[1])
SERVIDORTROZ = ListaInfo[0].split('@')
IP = SERVIDORTROZ[1]
Cliente = SERVIDORTROZ[0]
# print(SERVIDORTROZ)
# print (IP)
# print (Cliente)

if len(sys.argv) != 3:
    print("Usage: python client.py method receiver@IP:SIPport")
    sys.exit()


# Contenido que vamos a enviar
LINE = METODO + " sip:" + Cliente + "@" + IP + " SIP/2.0"

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

# print('Recibido --\r\n', data.decode('utf-8'))
print(data.decode('utf-8'))

if METODO == 'INVITE':
    Msj_ACK = data.decode('utf-8')
    Msj_ACK_Troz = Msj_ACK.split()
#   Miro en funcion de si es 100 180 o 200 para mandar el metodo
    Trying = Msj_ACK_Troz[1]
    Ring = Msj_ACK_Troz[4]
    OK = Msj_ACK_Troz[7]

#   ACK DEL INVITE
    if Trying == '100' and Ring == '180' and OK == '200':
        # print(Msj_ACK_Troz)
        LINE = 'ACK' + ' ' + 'sip:' + Cliente + '@' + IP + ' SIP/2.0'
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
        sys.exit()


print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
