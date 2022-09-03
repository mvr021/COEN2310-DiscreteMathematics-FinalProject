# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 09:13:11 2022

@author: yeya
"""

from program import *

menu = {
    1:'manual',
    2:'automático',
    3:'salir'
}

menu_datos = {
    1:'file_1.csv',
    2:'file_2.csv',
    3:'file_3.csv'
}

menu_umbral = {
    1:'promedio',
    2:'aleatorio',
    3:'máximo'
}

def print_menu():
    print('\nMenu:')
    for key in menu.keys():
        print (key, '--', menu[key])
        
def print_menu_datos():
    print('\nSubmenu:')
    for key in menu_datos.keys():
        print (key, '--', menu_datos[key])
        
def print_menu_umbral():
    print('\nSubmenu:')
    for key in menu_umbral.keys():
        print (key, '--', menu_umbral[key])
        
        
#Seleccionar y actuar        
flag = True

while flag == True:
    
    print_menu()
    opcion = int(input('Seleccione una opción: '))
   
    #Manual
    if opcion == 1:
        
        #selección de datos
        print_menu_datos()
        opcion_datos = int(input('Seleccione una opción: '))
        datos = menu_datos[opcion_datos]
        G = pd.read_csv(datos,header=None)
        
        #selección de umbral    
        print_menu_umbral()
        opcion_umbral = int(input('Seleccione una opción: '))
        
        if opcion_umbral == 1:
            th = promedio_umbral(G)
            
        elif opcion_umbral == 2:
            th = aleatorio_umbral(G)
            
        elif opcion_umbral == 3:
            th = max_umbral(G)
            
        else:
            print('Opción inválida. Reinicie.')
            continue
        
        P = algoritmo(G,th)
        
    #Automático
    elif opcion == 2:
        
        for key in menu_datos.keys():
            print("\n",menu_datos[key])
            G = pd.read_csv(menu_datos[key],header=None)
            th = promedio_umbral(G)
            P = algoritmo(G,th)
        
    #Salir
    elif opcion == 3:
        print('\nSaliendo...\n')
        flag = False
        
    else:
        print('Opción inválida. Ingrese un número entre 1 y 3.')

   