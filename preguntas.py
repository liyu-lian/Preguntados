import pygame
from constantes_preguntados import *

def tomar_datos(clave):
    lista_dato = []

    for elemento in lista:
        lista_dato.append(elemento[clave])

    return lista_dato


class Preguntas:
    def __init__(self):
        self.preguntas = tomar_datos("pregunta")
        self.respuestas_a = tomar_datos("a")
        self.respuestas_b = tomar_datos("b")
        self.respuestas_c = tomar_datos("c")
        self.correctas = tomar_datos("correcta")
        self.posicion = 0
        self.posicion_correcta = 0

        self.pregunta = self.preguntas[self.posicion]
        self.respuesta_a = self.respuestas_a[self.posicion]
        self.respuesta_b = self.respuestas_b[self.posicion]
        self.respuesta_c = self.respuestas_c[self.posicion]

    def pasar_pregunta(self):
        if self.posicion < len(self.preguntas)-1:
            self.posicion += 1
        return self.posicion
    
    def reiniciar_posicion(self):
        self.posicion = 0
        return self.posicion

    def rendear_preguntas(self,fuente):
        self.pregunta = self.preguntas[self.posicion]
        self.respuesta_a = self.respuestas_a[self.posicion]
        self.respuesta_b = self.respuestas_b[self.posicion]
        self.respuesta_c = self.respuestas_c[self.posicion]

        pregunta = fuente.render(str(self.pregunta),True,COLOR_NEGRO)
        respuesta_a = fuente.render(str(self.respuesta_a),True,COLOR_NEGRO)
        respuesta_b = fuente.render(str(self.respuesta_b),True,COLOR_NEGRO)
        respuesta_c = fuente.render(str(self.respuesta_c),True,COLOR_NEGRO)
        
        return pregunta, respuesta_a, respuesta_b, respuesta_c
    
    def get_correcta(self,posicion):
        self.correcta = self.correctas[posicion]
        return self.correcta


    def blitear_preguntas(self,pantalla, pregunta,respuesta_a,respuesta_b,respuesta_c):
        pantalla.blit(pregunta,POS_PREGUNTA)
        pantalla.blit(respuesta_a,POS_RESPUESTA_A)
        pantalla.blit(respuesta_b,POS_RESPUESTA_B)
        pantalla.blit(respuesta_c,POS_RESPUESTA_C)




