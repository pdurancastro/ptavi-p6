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
        #self.wfile.write(b"Hemos recibido tu peticion")
        cliente = self.rfile.read().decode('utf-8').split()
        print(cliente)
        
        
        metodo = cliente[0]
        if metodo == "INVITE":
            #Leyendo línea a línea lo que nos envía el cliente
            #line = self.rfile.read()
            print(metodo)
            
            #UN MENSAJE????????????????????????????????????????
            #------------------------------------------------------
            self.wfile.write(b"SIP/2.0 100 Trying\r\n")
            self.wfile.write(b"SIP/2.0 180 Ring\r\n")
            self.wfile.write(b"SIP/2.0 200 OK\r\n")
            #print("El cliente nos manda " + linea.decode('utf-8'))
            #------------------------------------------------------
        elif metodo == "BYE":
            print(metodo)
            self.wfile.write(b"SIP/2.0 200 OK\r\n")
        
        elif metodo == "ACK":
            print(metodo)
        else:
            print("NO ES EL METODO CORRECTO")
            self.wfile.write(b"IP/2.0 405 Method Not Allowed\r\n") 

    
    
if __name__ == "__main__":
    IP = (sys.argv[1])
    PUERTO = int(sys.argv[2])
    #print(IP + " " + str(PUERTO))
    
    if len(sys.argv[0:4]) != 4:
        #Deberia comprobar tambn si existe el fichero de audio
        print("Usage: python server.py IP port audio_file")
        sys.exit()
    
    print("Listening...")
 
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', PUERTO), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
