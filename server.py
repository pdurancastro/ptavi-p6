#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        # self.wfile.write(b"Hemos recibido tu peticion")
        cliente = self.rfile.read().decode('utf-8').split()
        print(cliente)

        metodo = cliente[0]
        if metodo == "INVITE":
            # Leyendo línea a línea lo que nos envía el cliente
            # line = self.rfile.read()
            print(metodo)

            self.wfile.write(b"SIP/2.0 100 Trying\r\n\r\n")
            self.wfile.write(b"SIP/2.0 180 Ring\r\n\r\n")
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

            # print("El cliente nos manda " + linea.decode('utf-8'))

        elif metodo == "BYE":
            print(metodo)
            self.wfile.write(b"SIP/2.0 200 OK\r\n")

        elif metodo == "ACK":
            print(metodo)
            AUDIO = (sys.argv[3])
            aEjecutar = 'mp32rtp -i ' + IP + ' -p 23032 < ' + AUDIO
            print("Vamos a ejecutar", aEjecutar)
            os.system(aEjecutar)

        elif metodo != "BYE" or metodo != "ACK" or metodo != "INVITE":
            print("NO ES EL METODO CORRECTO")
            self.wfile.write(b"SIP/2.0 405 Method Not Allowed\r\n\r\n")
        else:
            print("No estan bien escritos los argumentos")
            self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")


if __name__ == "__main__":
    IP = (sys.argv[1])
    PUERTO = int(sys.argv[2])
    # print(IP + " " + str(PUERTO))

    if len(sys.argv[0:4]) != 4 or len(sys.argv) > 4:
        # Deberia comprobar tambn si existe el fichero de audio
        print("Usage: python server.py IP port audio_file")
        sys.exit()

    print("Listening...")

    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', PUERTO), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
