import pygame
from botones import * 
from preguntas import *

pregunta = Preguntas()

class Jugador:
    def __init__(self):
        self.puntaje = 0
        self.intentos = 2

    def administrar_puntos(self, letra,posicion):
        correcta = pregunta.get_correcta(posicion=posicion)
        if letra == correcta:
            self.puntaje += 10
        else:
            self.intentos -= 1

        return self.puntaje, self.intentos
    
    def reiniciar(self):
        self.puntaje = 0
        self.intentos = 2
        return self.puntaje, self.intentos
    
    def perder(self,pantalla,fondo):
        if self.intentos == 0:
            pantalla.blit(fondo,fondo.get_rect())

    def ganar(self,pantalla,fondo):
        if self.puntaje == 160:
            pantalla.blit(fondo,fondo.get_rect())

    def rendear_puntos(self,fuente):
        puntaje_numerico = fuente.render(str(self.puntaje), True, (COLOR_BLANCO))
        intento_numerico = fuente.render(str(self.intentos), True, (COLOR_BLANCO))
        return puntaje_numerico, intento_numerico

    def mostrar_puntos(self,pantalla,puntaje_numerico, intento_numerico,fuente):
        puntos = fuente.render("Puntos: ", True, (COLOR_BLANCO))
        intentos = fuente.render("intentos: ", True, (COLOR_BLANCO))
        pantalla.blit(puntos, POS_PUNTOS)
        pantalla.blit(puntaje_numerico, POS_NUM_PUNTOS)
        pantalla.blit(intentos, POS_VIDAS)
        pantalla.blit(intento_numerico, POS_NUM_VIDAS)