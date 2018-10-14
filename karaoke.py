#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler


orden = sys.argv

if __name__ == "__main__":
    try:
        parser = make_parser()
        cHandler = smallsmilhandler.SallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(orden[1]))
        lista = cHandler.get_tags()
        for elemento in lista:
            etiqueta = elemento[0]
            print (etiqueta + '\t'),
            elementos = ""
            diccionario = elemento[1]
            for atributos in diccionario.keys():
                elementos = elementos + atributos + '=' + '"' + elemento[1][atributos] + '"' + '\t'
            print (elementos)