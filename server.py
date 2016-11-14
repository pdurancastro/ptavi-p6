#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        cliente = self.rfile.read().decode('utf-8').split()
        #print(cliente)
        
        
        metodo = cliente[0]
        if metodo == "INVITE":
        #while 1:
            #Leyendo línea a línea lo que nos envía el cliente
            #line = self.rfile.read()
            print(metodo)
            #print("El cliente nos manda " + linea.decode('utf-8'))
        
        elif metodo == "BYE":
            print(metodo)
        
        elif metodo == "ACK":
            print(metodo)
        
        else:
            print("NO ES EL METODO CORRECTO")

            # Si no hay más líneas salimos del bucle infinito
            #if not line:
                #break

if __name__ == "__main__":
    IP = (sys.argv[1])
    PUERTO = int(sys.argv[2])
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', PUERTO), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
