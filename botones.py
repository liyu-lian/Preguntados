import pygame
from constantes_preguntados import *
from preguntas import Preguntas
from jugador import Jugador

pregunta = Preguntas()
jugador = Jugador()

class Botones:
    def __init__(self):
        self.boton_vacio = pygame.image.load(PATH_BOTON+"3.png")
        self.boton_pregunta = pygame.image.load(PATH_BOTON+"1.png")
        self.boton_reiniciar = pygame.image.load(PATH_BOTON+"2.png")

        self.rect_btn_pregunta = pygame.Rect(RECT_PREGUNTA)
        self.rect_btn_reiniciar = pygame.Rect(RECT_REINICIAR)
        self.rect_btn_A = pygame.Rect(RECT_A)
        self.rect_btn_B = pygame.Rect(RECT_B)
        self.rect_btn_C = pygame.Rect(RECT_C)

        self.posicion_correcta = 0
        # self.bloquear_suma = False

    def dibujar_boton(self,pantalla,posicion,boton):
        if boton == "reiniciar":
            boton = self.boton_reiniciar
        elif boton == "pregunta":
            boton = self.boton_pregunta
        elif boton == "vacio":
            boton = self.boton_vacio

        pantalla.blit(boton,posicion)
        # pygame.draw.rect(pantalla,COLOR_NEGRO,(RECT_PREGUNTA),2)
        # pygame.draw.rect(pantalla,COLOR_NEGRO,(RECT_REINICIAR),2)
        # pygame.draw.rect(pantalla,COLOR_ROJO,(RECT_A),2)
        # pygame.draw.rect(pantalla,COLOR_ROJO,(RECT_B),2)
        # pygame.draw.rect(pantalla,COLOR_ROJO,(RECT_C),2)

    def dibujar_recuadro(self,pantalla,posicion):
        recuadro = pygame.image.load(PATH_BOTON+"recuadro.png")
        pantalla.blit(recuadro,posicion)

    def interactuar_boton(self,evento,fuente):
        x, y = evento

        if self.rect_btn_pregunta.collidepoint(x, y):
            posicion = pregunta.pasar_pregunta()
            lista_render = pregunta.rendear_preguntas(fuente)
            jugador.activar_interaccion()
            self.posicion_correcta = posicion
        elif self.rect_btn_reiniciar.collidepoint(x,y):
            pregunta.reiniciar_posicion()
            jugador.reiniciar()
            lista_puntos_vida = jugador.rendear_puntos(fuente=fuente)
            lista_render = pregunta.rendear_preguntas(fuente)
        else:
            lista_render = pregunta.rendear_preguntas(fuente)

        
        if self.rect_btn_A.collidepoint(x,y):
            jugador.administrar_puntos("a",self.posicion_correcta)
            lista_puntos_vida = jugador.rendear_puntos(fuente=fuente)
            jugador.desactivar_interaccion()
        elif self.rect_btn_B.collidepoint(x,y):
            jugador.administrar_puntos("b",self.posicion_correcta)
            lista_puntos_vida = jugador.rendear_puntos(fuente=fuente)
            jugador.desactivar_interaccion()
        elif self.rect_btn_C.collidepoint(x,y):
            jugador.administrar_puntos("c",self.posicion_correcta)
            lista_puntos_vida = jugador.rendear_puntos(fuente=fuente)
            jugador.desactivar_interaccion()
        else:
            lista_puntos_vida = jugador.rendear_puntos(fuente=fuente)

        return lista_render, lista_puntos_vida
