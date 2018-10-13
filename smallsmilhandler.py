#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para el manejo de Smill
    """
    
    def __init__(self):
        
        self.tags = []
        self.Diccionario = {
            'root-layout': ['width', 'height', 'background_color'],
            'region': ['id', 'top', 'bottom', 'left', 'right'],
            'img': ['src', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']}
    
    
    def startElement(self, name, attrs):
         
         if name in self.Diccionario:
             tmpdicc = {}
             for atributo in self.Diccionario[name]:
                 tmpdicc[atributo] = attrs.get(atributo, "")
             self.tags.append([name, tmpdicc])
             
    def get_tags(self):
         return self.tags
         
         

if __name__ == "__main__":
       """
       Programa principal
       """
       parser = make_parser()
       cHandler = SmallSMILHandler()
       parser.setContentHandler(cHandler)
       parser.parse(open('karaoke.smil'))
       print(cHandler.get_tags())
    
   
