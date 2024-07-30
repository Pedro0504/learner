# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:46:20 2024

@author: pedro
"""
#importamos el módulo random
import random as rd

#declaramos una variable de forma afirmativa
juego_nuevo = input("Quieres jugar:(si/no)\n")
#la variable sirve para inicie el while loop
#que se repite mientras la pregunta de juegar nuevamente sea afirmativa
while juego_nuevo == "si":  
    #se inician variables ronda, y jugadores
    #que sirven para contar las rondas y las victorias
    ronda = 1
    print("RONDA NO.1")
    jugador_1 = 0
    jugador_2 = 0
    #iniciamos un loop while para que realice el juego durante
    #5 turnos
    while ronda<6:
        jugadas1=[]
        jugadas2=[]
        #se habilitan variables jugadas 1 y 2 
        #así como doble para guardar las 
        #tiradas de los dados de ambos jugadores
        #que se generan en un for loop
        for i in range (0,2):
            tiros_1 = rd.randint(1,6)
            jugadas1.append(tiros_1)
        for i in range (0,2):
            tiros_2 = rd.randint(1,6)
            jugadas2.append(tiros_2)
        doble =[]
        for i in jugadas1:
            if jugadas1.count(i)>1:
                doble.append(i)
            else:
                pass
        for i in jugadas2:
            if jugadas2.count(i)>1:
                doble.append(i)
            else:
                pass
        #se declara comparación para saber si algu valor se repite
        #valor que se busca en el siguiente for loop
        comparacion = []    
        print(jugadas1, "y", jugadas2)
        for n in jugadas1:
            for m in jugadas2:
                if n==m:
                    comparacion.append(n)
                else:
                    pass
        #si el largo de la lista comparación es mayor a cero, 
        #indica coincidencia, de lo contrario no existe,
        #de ahí que el condicional if otorgue puntos de acuerdo
        #a las reglas del juego
        if (len(comparacion)>0) or (len(doble)>0):
            print("El jugador 1 gana.\n")
            jugador_1 = jugador_1 + 1 
        else:
            print("el jugador 2 gana.\n")
            jugador_2 = jugador_2 + 1
        #el siguiente condicional revisa la puntuación y declara
        #el ganador absoluto
        if jugador_1 == 3:
            print("El ganador absoluto es el Jugador 1.\n")
            break
        elif jugador_2 == 3:
            print("El ganador absoluto es el Jugador 2.\n")
            break
        #los siguientes comandos elevan la ronda y la declaran
        ronda = ronda+1
        print(f"RONDA NO. {ronda}")
    juego_nuevo = input("Quieres jugar:(si/no)\n")
            

