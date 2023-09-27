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

#imagen
imagen = pygame.image.load("Trivia-Crack-F.png")
imagen = pygame.transform.scale(imagen, (300, 300))

#pantalla y ventana
pantalla = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Preguntados")
pygame.display.set_icon(imagen)

#Fuentes
fuente = pygame.font.SysFont("Times New Roman", 30)

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

comentario_fin = fuente.render("FIN DEL JUEGO.. Presione reiniciar para jugar otra vez", True, (COLOR_BLANCO))

#Puntos
punto_numerico = 0
puntos = fuente.render("Puntos: ", True, (COLOR_BLANCO))
puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))

posicion = 0

contador_fail = 0

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


            #posición de botone

            #Boton Preguntar
            if (click[0] > 498 and click[0] < 656) and (click[1] > 80 and click[1] < 181):
                
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

                #Permite que muestre todas las preguntas al apretar el btn
                if posicion < len(lista_preguntas)-1:
                    posicion +=1


            #Boton Reiniciar
            elif (click[0] > 799 and click[0] < 960) and (click[1] > 78 and click[1] < 178):
                
                posicion = 0
                punto_numerico = 0
                puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))
                contador_fail = 0

                pregunta = lista_preguntas[posicion]
                preguntas = fuente.render(str(pregunta), True, (COLOR_BLANCO))

                respuesta_A = lista_respuesta_a[posicion]
                respuesta_B = lista_respuesta_b[posicion]
                respuesta_C = listas_respuestas_c[posicion]
                correctas = listas_respuestas_correctas[posicion]

                respuesta_a = fuente.render(str(respuesta_A), True, (COLOR_BLANCO))
                respuesta_b = fuente.render(str(respuesta_B), True, (COLOR_BLANCO))
                respuesta_c = fuente.render(str(respuesta_C), True, (COLOR_BLANCO))

            #Boton A
            elif (click[0] > 99 and click[0] < 350) and (click[1] > 546 and click[1] < 648):

                #comparación y suma de puntos
                if  correctas == 'a':
                    punto_numerico += 10

                    puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))

                else:
                    contador_fail += 1


            #Boton B
            elif (click[0] > 499 and click[0] < 748) and (click[1] > 546 and click[1] < 700):
                
                if  correctas == 'b':
                    punto_numerico += 10

                    puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))

                else:
                    contador_fail += 1

            #Boton C
            elif (click[0] > 900 and click[0] < 1150) and (click[1] > 548 and click[1] < 700):

                if  correctas == 'c':
                    punto_numerico += 10

                    puntaje_numerico = fuente.render(str(punto_numerico), True, (COLOR_BLANCO))
                    
                else:
                    contador_fail += 1

            #Hace que cuando se acabe la lista vuelva a 0
            elif posicion > len(lista_preguntas)-1:
                posicion = 0


    #Rellenar la pantalla de un color
    pantalla.fill(COLOR_PANTALLA)

    #rectángulo pregunta
    pygame.draw.rect(pantalla, (143, 191, 201), (498,80,160,100))
    #rectángulo reiniciar
    pygame.draw.rect(pantalla, (143, 191, 201), (800,80,160,100))
    #rectángulo A
    pygame.draw.rect(pantalla, (143, 191, 201), (100, 550, 250, 150))
    #rectángulo B
    pygame.draw.rect(pantalla, (143, 191, 201), (500, 550, 250, 150))
    #rectángulo C
    pygame.draw.rect(pantalla, (143, 191, 201), (900, 550, 250, 150))

    #fundir textos en pantalla
    pantalla.blit(imagen, (20,20))
    pantalla.blit(boton_pregunta, (522,110))
    pantalla.blit(boton_reiniciar, (825,110))
    pantalla.blit(puntos, (495, 200))

    #hace que desaparezcan los textos y muestre un mensaje en caso de perder
    if contador_fail < 2:
        pantalla.blit(preguntas, (350, 410))
        pantalla.blit(respuesta_a, (175, 600))
        pantalla.blit(respuesta_b, (575, 600))
        pantalla.blit(respuesta_c, (975, 600))
    else:
        pantalla.blit(comentario_fin, (350, 410))

    pantalla.blit(puntaje_numerico, (495, 300))


    pygame.display.flip()

pygame.quit()
#Fin del Juego
