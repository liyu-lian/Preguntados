import pygame
from constantes_preguntados import *
from botones import *
from preguntas import *

preguntas = Preguntas()
botones = Botones()

pygame.init()

#Imagenes
icon = pygame.image.load(PATH+"icon.jpg")
fondo = pygame.image.load(PATH+"nuevo_trauma.jpg")
fondo_perder = pygame.image.load(PATH+"you_died.jpg")
fondo = pygame.transform.scale(fondo,TAMAÑO_VENTANA)
fondo_perder = pygame.transform.scale(fondo_perder,TAMAÑO_VENTANA)
fondo_ganar = pygame.image.load(PATH+"ganaste.jpg")

#Fuente
fuente = pygame.font.SysFont("Bebas-Neue Regular", 40)

pantalla = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Preguntados Remastered")
pygame.display.set_icon(icon)

lista_render = pregunta.rendear_preguntas(fuente=fuente)

lista_render_puntos_vida = jugador.rendear_puntos(fuente=fuente)

flag_correr = True

while flag_correr:
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = list(evento.pos)
            print(click)

            #Interactuar botones
            lista_render, lista_render_puntos_vida = botones.interactuar_boton(evento=evento.pos,fuente=fuente)

    #Boton Pregunta
    botones.dibujar_boton(pantalla=pantalla,posicion=(420,80),boton="pregunta")
    #Recuadro Pregunta
    botones.dibujar_recuadro(pantalla,(110,300))
    #Botón A
    botones.dibujar_boton(pantalla=pantalla,posicion=(80, 600),boton="vacio")
    #Botón B
    botones.dibujar_boton(pantalla=pantalla,posicion=(450, 600),boton="vacio")
    #Botón C
    botones.dibujar_boton(pantalla=pantalla,posicion=(830, 600),boton="vacio")

    #Blitear Preguntas
    preguntas.blitear_preguntas(pantalla,lista_render[0],lista_render[1],lista_render[2],lista_render[3])

    #Pantalla perder
    jugador.perder(pantalla=pantalla,fondo=fondo_perder)
    #Pantalla ganar
    jugador.ganar(pantalla=pantalla,fondo=fondo_ganar)

    #Blitear puntos
    jugador.mostrar_puntos(pantalla,lista_render_puntos_vida[0],lista_render_puntos_vida[1],fuente)

    #Boton Reiniciar
    botones.dibujar_boton(pantalla=pantalla,posicion=(800,80),boton="reiniciar")

    pygame.display.flip()

    pantalla.blit(fondo, fondo.get_rect())

pygame.quit()