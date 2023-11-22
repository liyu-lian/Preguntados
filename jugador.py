import pygame
from preguntas import *

pregunta = Preguntas()

class Jugador:
    def __init__(self):
        self.puntaje = 0
        self.intentos = 2
        self.interaccion_activa = True

    def administrar_puntos(self, letra, posicion):
        correcta = pregunta.get_correcta(posicion=posicion)

        if self.interaccion_activa:
            if letra == correcta:
                self.puntaje += 10
            else:
                self.intentos -= 1

        return self.puntaje, self.intentos

    def reiniciar(self):
        self.puntaje = 0
        self.intentos = 2
        self.activar_interaccion()  # Reset the interaction state
        return self.puntaje, self.intentos

    def activar_interaccion(self):
        self.interaccion_activa = True

    def desactivar_interaccion(self):
        self.interaccion_activa = False

    def inhabilitar_acciones(self):
        self.desactivar_interaccion()

    def habilitar_acciones(self):
        self.activar_interaccion()

    def perder(self, pantalla, fondo):
        if self.intentos == 0:
            pantalla.blit(fondo, fondo.get_rect())
            self.inhabilitar_acciones()  # Disable interaction on loss

    def ganar(self, pantalla, fondo):
        if self.puntaje == 160:
            pantalla.blit(fondo, fondo.get_rect())
            self.inhabilitar_acciones()  # Disable interaction on win

    def rendear_puntos(self, fuente):
        puntaje_numerico = fuente.render(str(self.puntaje), True, (COLOR_BLANCO))
        intento_numerico = fuente.render(str(self.intentos), True, (COLOR_BLANCO))
        return puntaje_numerico, intento_numerico

    def mostrar_puntos(self, pantalla, puntaje_numerico, intento_numerico, fuente):
        puntos = fuente.render("Puntos: ", True, (COLOR_BLANCO))
        intentos = fuente.render("intentos: ", True, (COLOR_BLANCO))
        pantalla.blit(puntos, POS_PUNTOS)
        pantalla.blit(puntaje_numerico, POS_NUM_PUNTOS)
        pantalla.blit(intentos, POS_VIDAS)
        pantalla.blit(intento_numerico, POS_NUM_VIDAS)