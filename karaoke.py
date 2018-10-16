#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from smallsmilhandler import SmallSMILHandler
import sys
import os
import json

class KaraokeLocal():
    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        try:
            parser.parse(open(fichero))
            self.lista = cHandler.get_tags()
        except IOError:
            sys.exit("Error del fichero")
        

    def __str__(self):
        
        salida = ""
        for elemento in self.lista:
            nombre = elemento['etiqueta']
            salida == nombre
            for atributo in elemento:
                if atributo != "etiqueta" and elemento [atributo] != "":
                    salida == "\t" + atributo + ":" + elemento[atributo]
            salida == "\n"
        
        return salida

    def do_local(self):
        for elemento in self.lista:
            nombre = elemento['etiqueta']
            for atributo in elemento:
                if atributo == "src":
                    recurso = elemento['src'] 
                    os.system("wget -q" + recurso)
                    recurso = recurso.split("/")[-1]
                    elemento["src"] = recurso
        return self.lista
                    
    
    def to_json(self, fichero):
        "Convertir SMIL a JSON"
        nuevojson = json.dumps(self.lista)
        nombrefichero = fichero.split('.')[0] + '.json'
        with open(nombrefichero, 'w') as ficherojson:
            json.dump(nuevojson, ficherojson)

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
    except IndexError:
        print("Usage: python karaoke.py file.smil")
    karaoke = KaraokeLocal(fichero)
    print(karaoke.__str__())
    karaoke.to_json(fichero)
    karaoke.to_json("local.json")
    karaoke.do_local()
    print(karaoke)
                       