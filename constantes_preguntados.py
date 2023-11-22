import pygame

TAMAÑO_VENTANA = (1200, 1000)
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_MORADO= (79, 60, 86)
COLOR_BOTONES = (179, 156, 187)
COLOR_ROJO = (255,0,0)

MENSAJE_FINAL = "PERDISTE.. Presioná reiniciar para jugar otra vez"

MENSAJE_GANADOR = "Lo haz logrado! Juega otra vez.. (reiniciar)"

PATH = "./imagenes/"
PATH_BOTON = "./imagenes/botones/"

POS_PUNTOS = (255,75)
POS_NUM_PUNTOS = (255,130)
POS_VIDAS = (95,75)
POS_NUM_VIDAS = (100,130)
POS_PREGUNTA = (180,350)
POS_RESPUESTA_A= (150, 610)
POS_RESPUESTA_B = (500, 610)
POS_RESPUESTA_C = (900, 610)
RECT_PREGUNTA = (420,80,275,109)
RECT_REINICIAR = (800,80,275,109)
RECT_A = (80,600,275,109)
RECT_B = (450,600,275,109)
RECT_C = (830,600,275,109)

lista=[{'pregunta': '¿Cuál es la moneda de México?', 'a': 'Peso', 'b': 'Dolar', 'c':'Euro' ,'correcta': 'a'}, 
{'pregunta': '¿De qué colores es la bandera de Japón?', 'a': 'Azul y Amarilla','b': 'Blanca y roja', 'c':'Celeste y Blanca' ,'correcta': 'b'}, 
{'pregunta': '¿Cuántos elementos forman la Tabla Periódica?', 'a': '118', 'b': '123', 'c':'125' ,'correcta': 'a'},
{'pregunta': '¿Quién pintó la Mona Lisa?', 'a': 'Dali', 'b': 'Miguel Angel', 'c':'Leonardo da Vinci' ,'correcta': 'c'},
{'pregunta': '¿Qué elemento de la tabla periódica tiene como símbolo He?', 'a': 'Hielo', 'b': 'Helio', 'c':'Litio' ,'correcta': 'b'},
{'pregunta': '¿Qué planeta es el que se encuentra más cerca del Sol?', 'a': 'Mercurio', 'b': 'Marte', 'c':'Jupiter' ,'correcta': 'a'},
{'pregunta': '¿A cuántos kilómetros equivale una milla?', 'a': '3.6 km.', 'b': '2.6 km.', 'c':'1.6 km.' ,'correcta': 'c'},
{'pregunta': '¿De dónde es originario el mojito?', 'a': 'Cuba', 'b': 'Puerto Rico', 'c':'El Salvador' ,'correcta': 'a'},
{'pregunta': '¿Cuántos lados tiene un heptadecágono?', 'a': 'Dieciseis', 'b': 'Diecisete', 'c':'Quince' ,'correcta': 'b'},
{'pregunta': '¿De dónde sale el aceite de oliva?', 'a': 'aceitunas', 'b': 'girasol', 'c':'maiz' ,'correcta': 'a'},
{'pregunta': '¿Dónde nació la pizza?', 'a': 'Roma', 'b': 'Venecia', 'c':'Napoles' ,'correcta': 'c'},
{'pregunta': '¿Cuál es la capital de Kenia?', 'a': 'Luanda', 'b': 'Nairobi', 'c':'El Cairo' ,'correcta': 'b'},
{'pregunta': '¿Cuántos colores tiene el cubo Rubik?', 'a': '6', 'b': '9', 'c':'4' ,'correcta': 'a'},
{'pregunta': '¿A qué país pertenece la Isla de Pascua?', 'a': 'Argentina', 'b': 'Chile', 'c':'Brasil' ,'correcta': 'b'},
{'pregunta': '¿Cuál es el país más grande del mundo?', 'a': 'China', 'b': 'Canada', 'c':'Rusia' ,'correcta': 'c'},
{'pregunta': '¿Cuál es el lugar más frío de la tierra?', 'a': 'Rusia', 'b': 'Antartida', 'c':'Groenlandia' ,'correcta': 'b'},
{'pregunta': '¿Cuál es el río más largo del planeta?', 'a': 'Amazonas', 'b': 'Nilo', 'c':'Misisipi' ,'correcta': 'a'}]
