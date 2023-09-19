from lista_preguntados import lista

from constantes_preguntados import * 

import pygame

pregunta = ""
A = ""
B = ""
C = ""

acumulador_score = 0

contador_fail = 0

posiciones = 0

lista_preguntas = []
lista_respuestas_a = []
lista_respuestas_b = []
lista_respuestas_c = []
lista_correctas = []


for preguntas in lista:
    lista_preguntas.append(preguntas["pregunta"])
    lista_respuestas_a.append(preguntas["a"])
    lista_respuestas_b.append(preguntas["b"])
    lista_respuestas_c.append(preguntas["c"])
    lista_correctas.append(preguntas["correcta"])


pygame.init()

#declaración de variables 

imagen = pygame.image.load("Trivia-Crack-F.png")

pantalla = pygame.display.set_mode(TAMAÑO_VENTANA)
pygame.display.set_caption("Preguntados")
pygame.display.set_icon(imagen)

imagen = pygame.transform.scale(imagen,(300, 300))

FUENTE = pygame.font.SysFont("Times New Roman", 30)

FUENTE_PREGUNTA = pygame.font.SysFont("Times New Roman", 30)

FUENTE_RESPUESTA = pygame.font.SysFont("Times New Roman", 30)

boton_pregunta = FUENTE.render("Pregunta", True, (COLOR_BLANCO))

boton_reiniciar = FUENTE.render("Reiniciar", True, (COLOR_BLANCO))

puntos = FUENTE.render("Score: ", True, (COLOR_BLANCO))

preguntita = FUENTE.render(str(pregunta), True, (COLOR_BLANCO))

respuesta_A = FUENTE.render(str(A), True, (COLOR_BLANCO))
respuesta_B = FUENTE.render(str(B), True, (COLOR_BLANCO))
respuesta_C = FUENTE.render(str(C), True, (COLOR_BLANCO))

flag_correr = True

while flag_correr:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            flag_correr = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            click = list(evento.pos) #Interaccion del cursor con la pantalla
            print(click)

            # Boton pregunta. Muestra las preguntas al presionar el botón
            if (click[0] > 498 and click[0] < 656 and click[1] > 80 and click[1] < 181):

                pregunta = lista_preguntas[posiciones]
                preguntita = FUENTE_PREGUNTA.render(str(pregunta), True, (COLOR_BLANCO))

                A = lista_respuestas_a[posiciones]
                B = lista_respuestas_b[posiciones]
                C = lista_respuestas_c[posiciones]

                respuesta_A = FUENTE_RESPUESTA.render(str(A), True, (COLOR_BLANCO))
                respuesta_B = FUENTE_RESPUESTA.render(str(B), True, (COLOR_BLANCO))
                respuesta_C = FUENTE_RESPUESTA.render(str(C), True, (COLOR_BLANCO))

                if posiciones < len(lista_preguntas):
                    posiciones += 1
            
            #Boton de reinicio. Vuelve al índice 0 de lista_preguntas.
            elif(click[0] > 799 and click[0] < 960 and click[1] > 78 and click[1] < 178):
                posiciones = 0

                pregunta = lista_preguntas[posiciones]
                preguntita = FUENTE_PREGUNTA.render(str(pregunta), True, (COLOR_BLANCO))

                A = lista_respuestas_a[posiciones]
                B = lista_respuestas_b[posiciones]
                C = lista_respuestas_c[posiciones]

                respuesta_A = FUENTE_RESPUESTA.render(str(A), True, (COLOR_BLANCO))
                respuesta_B = FUENTE_RESPUESTA.render(str(B), True, (COLOR_BLANCO))
                respuesta_C = FUENTE_RESPUESTA.render(str(C), True, (COLOR_BLANCO)) 

            
            if posiciones > len(lista_preguntas) -1:
                posiciones = 0


    #asignar respuesta a Botón
            if (click[0] > 633 and click[0] < 749) and (click[0] > 630 and click[0] < 697):
                pass
            elif (click[0] > 499 and click[0] < 748) and (click[0] > 546 and click[0] < 700):
                pass
            elif (click[0] > 900 and click[0] < 1150) and (click[0] > 548 and click[0] < 700):
                pass


    pantalla.fill(COLOR_PANTALLA)

    pygame.draw.rect(pantalla, (143, 191, 201), (498,80,160,100))
    pygame.draw.rect(pantalla, (143, 191, 201), (800,80,160,100))

    pygame.draw.rect(pantalla, (143, 191, 201), (100, 550, 250, 150))
    pygame.draw.rect(pantalla, (143, 191, 201), (500, 550, 250, 150))
    pygame.draw.rect(pantalla, (143, 191, 201), (900, 550, 250, 150))

    pantalla.blit(imagen,(20,20))
    pantalla.blit(boton_pregunta, (522,110))
    pantalla.blit(boton_reiniciar, (825,110))
    pantalla.blit(puntos, (495, 200))
    pantalla.blit(preguntita, (350, 410))
    pantalla.blit(respuesta_A, (175, 600))
    pantalla.blit(respuesta_B, (575, 600))
    pantalla.blit(respuesta_C, (975, 600))
    

    pygame.display.flip()

pygame.quit()
#Fin del juego