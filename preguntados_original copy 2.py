from lista_preguntados import lista
from constantes_preguntados import *
import pygame

lista_preguntas = []
lista_respuesta_a = []
lista_respuesta_b = []
listas_respuestas_c = []
listas_respuestas_correctas = []

for valores in lista:
    lista_preguntas.append(valores["pregunta"])
    lista_respuesta_a.append(valores["a"])
    lista_respuesta_b.append(valores["b"])
    listas_respuestas_c.append(valores["c"])
    listas_respuestas_correctas.append(valores["correcta"])


pygame.init()

#imagenese
imagen = pygame.image.load("burro.jpg")
imagen = pygame.transform.scale(imagen, (250, 250))
imagen_fin = pygame.image.load("you_died.jpg")
imagen_ganador = pygame.image.load("ganaste.jpg")

#pantalla y ventana
pantalla = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Preguntados")
pygame.display.set_icon(imagen)

#Fuentes
fuente = pygame.font.SysFont("Times New Roman", 30)
fuente_fin = pygame.font.SysFont("Tahoma", 30)

#Textos
boton_pregunta = fuente.render("Pregunta", True, (COLOR_BLANCO))
boton_reiniciar = fuente.render("Reiniciar", True, (COLOR_BLANCO))

pregunta = ""
respuesta_A = ""
respuesta_B = ""
respuesta_C = ""
correctas = ""

preguntas = fuente.render(str(pregunta), True, (COLOR_BLANCO))
respuesta_a = fuente.render(str(respuesta_A), True, (COLOR_BLANCO))
respuesta_b = fuente.render(str(respuesta_B), True, (COLOR_BLANCO))
respuesta_c = fuente.render(str(respuesta_C), True, (COLOR_BLANCO))

comentario_fin = fuente_fin.render(str(MENSAJE_FINAL), True, (187, 43, 72))

comentario_ganador = fuente.render(str(MENSAJE_GANADOR), True, (152, 124, 53))

#Puntos
punto_numerico = 0
puntos = fuente.render("Puntos: ", True, (COLOR_BLANCO))
puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))

posicion = 0

contador_fail = 0

bandera_comience = False

bandera_preguntar =  False

color_boton = (179, 156, 187)

#Linea necesaria para poder cerrar el juego
flag_correr = True

while flag_correr:

    # Lineas necesarias para cerrar el juego
    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            flag_correr = False

        #Interacción del cursor con la pantalla
        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = list(evento.pos)
            #posición de boton

            #Boton Preguntar
            if (click[0] > 498 and click[0] < 656) and (click[1] > 80 and click[1] < 181) and bandera_preguntar == False:
            
                if bandera_comience == False:
                
                    pregunta = lista_preguntas[posicion]
                    preguntas = fuente.render(str(pregunta), True, (COLOR_BLANCO))
                    contador_fail = 0

                    respuesta_A = lista_respuesta_a[posicion]
                    respuesta_B = lista_respuesta_b[posicion]
                    respuesta_C = listas_respuestas_c[posicion]
                    correctas = listas_respuestas_correctas[posicion]

                    respuesta_a = fuente.render(str(respuesta_A), True, (COLOR_BLANCO))
                    respuesta_b = fuente.render(str(respuesta_B), True, (COLOR_BLANCO))
                    respuesta_c = fuente.render(str(respuesta_C), True, (COLOR_BLANCO))

                    bandera_comience = True

                #Permite que muestre todas las preguntas al apretar el btn
                if posicion < len(lista_preguntas)-1:
                    posicion +=1

            #Boton Reiniciar
            elif (click[0] > 799 and click[0] < 960) and (click[1] > 78 and click[1] < 178):
                #bandera usada para que no pase a la siguiente pregunta si no respondió bien
                bandera_comience = True
                #bandera usada para que no permitar pasar pregunta o sumar puntos en caso de perder
                bandera_preguntar = False
                posicion = 0
                punto_numerico = 0
                contador_fail = 0
                color_boton = (179, 156, 187)

                pregunta = lista_preguntas[posicion]
                respuesta_A = lista_respuesta_a[posicion]
                respuesta_B = lista_respuesta_b[posicion]
                respuesta_C = listas_respuestas_c[posicion]
                correctas = listas_respuestas_correctas[posicion]

                puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))
                preguntas = fuente.render(str(pregunta), True, (COLOR_BLANCO))
                respuesta_a = fuente.render(str(respuesta_A), True, (COLOR_BLANCO))
                respuesta_b = fuente.render(str(respuesta_B), True, (COLOR_BLANCO))
                respuesta_c = fuente.render(str(respuesta_C), True, (COLOR_BLANCO))

                posicion += 1

            #Boton A
            if bandera_comience == True:
                if (click[0] > 99 and click[0] < 350) and (click[1] > 546 and click[1] < 648):
                #comparación y suma de puntos
                    if  correctas == 'a':
                        punto_numerico += 10
                        puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))
                        bandera_comience = False

                    else:
                        contador_fail += 1
                #Boton B
                elif (click[0] > 499 and click[0] < 748) and (click[1] > 546 and click[1] < 700):

                    if  correctas == 'b':
                        punto_numerico += 10
                        puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))
                        bandera_comience = False

                    else:
                        contador_fail += 1
                #Boton C
                elif (click[0] > 900 and click[0] < 1150) and (click[1] > 548 and click[1] < 700):

                    if  correctas == 'c':
                        punto_numerico += 10
                        puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))
                        bandera_comience = False

                    else:
                        contador_fail += 1

            #Hace que cuando se acabe la lista vuelva a 0
            elif posicion > len(lista_preguntas)-1:
                posicion = 0


    #Rellenar la pantalla de un color
    pantalla.fill(COLOR_PANTALLA)

    #hace que desaparezcan los textos y muestre un mensaje en caso de perder
    if contador_fail < 2:
        #rectángulo pregunta
        pygame.draw.rect(pantalla, (COLOR_BOTONES), (498,80,160,100))
        #rectángulo A
        pygame.draw.rect(pantalla, (COLOR_BOTONES), (100, 550, 250, 150))
        #rectángulo B
        pygame.draw.rect(pantalla, (COLOR_BOTONES), (500, 550, 250, 150))
        #rectángulo C
        pygame.draw.rect(pantalla, (COLOR_BOTONES), (900, 550, 250, 150))

        pantalla.blit(imagen, (100,60))
        pantalla.blit(boton_pregunta, (522,110))
        pantalla.blit(preguntas, (350, 410))
        pantalla.blit(respuesta_a, (175, 600))
        pantalla.blit(respuesta_b, (575, 600))
        pantalla.blit(respuesta_c, (975, 600))

        if punto_numerico > 160:
            pantalla.blit(imagen_ganador,(0,0))
            pantalla.blit(comentario_ganador,(680, 450))

            color_boton = (232, 171, 19)
    else:
        pantalla.blit(imagen_fin, (0,0))
        pantalla.blit(comentario_fin, (300, 450))
        color_boton = (89, 38, 48)
        bandera_comience = False
        bandera_preguntar = True

        

    #Boton reiniciar
    pygame.draw.rect(pantalla, (color_boton), (800,80,160,100))
    pantalla.blit(boton_reiniciar, (825,110))

    pantalla.blit(puntos, (495, 200))
    pantalla.blit(puntaje_numerico, (500, 250))


    pygame.display.flip()

pygame.quit()
#Fin del Juego
