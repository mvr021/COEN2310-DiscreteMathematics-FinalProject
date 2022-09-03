# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:10:23 2022

@author: yeya
"""
import pandas as pd
import random


def promedio_umbral(G):
    """Obtiene el valor promedio de las distancias del grafo G."""  
  
    number_list =[]
    for i in range(len(G)):
        for j in range(len(G)): 
            number = G[i][j]
            number_list.append(number)
             
    th = sum(number_list) / len(number_list)
    
    return th


def aleatorio_umbral(G):
    """Obtiene un valor de distancia aleatoriamente del grafo G."""  
    
    r1 = (random.randint(0,len(G)-1))
    r2 = (random.randint(0,len(G)-1))
    th = G[r1][r2]
    
    return th


def max_umbral(G):
    """Obtiene el valor máximo de las distancias del grafo G.""" 
    th = 0
    for i in range(len(G)):
        for j in range(len(G)): 
            number = G[i][j]
            if number > th:
                th = number
    
    return th


def find_max_degree(S,G,th):
    """Halla la matriz de adyacencia y el vertice con el mayor grado en C."""  
    adyacencia = []
    
    for i in S:
        A = []
        for j in S:
            d = G[i][j]
            if d < th and d != 0:
                a = 1
            else:
                a = 0
            A.append(a)
        adyacencia.append(A)
    adyacencia = pd.DataFrame(adyacencia)
    
    column_names=list(G.columns)
    adyacencia.columns = column_names
    adyacencia.index = column_names
    
    degree = adyacencia[adyacencia == 1].count()
    
    degree_list = [degree[r] for r in column_names]
    v_list = [m for m in column_names]
    
    max_degree = 0
    for number in degree_list: 
        
        if number > max_degree:
            max_degree = number
            
    v = v_list[degree_list.index(max_degree)]
        
    if max_degree == 0:
        v = column_names[0]
    
    return v


def cercano(th,C,S,G):
    """Encuentra el vertice x más cercano al grupo C. """  
    all_D = []
    min_D = []
    
    for j in S:
        sum_D = []
        D = []
        for i in C:
            distancia = G.loc[i,j]
            D.append(distancia)
        sum_D = sum(D)/len(C)
        all_D.append(sum_D)
        
    if len(all_D)!= 0:
        
        min_D = all_D[0]
        for number in all_D: 
            
            if number < min_D:
                min_D = number
                
        index_D = all_D.index(min_D)

        if min_D <= th:
            x = S[index_D]
            b = 1
        else:
            x = S[index_D]
            b = 0   
    else:
        x = 0
        b = 0

    return b,x

  
def algoritmo(G,th):
    """Transforma una matriz de distancias en un grafo conectado."""  
    S = list(range(len(G)))
    P = []
    t = 0
    
    while len(S) != 0 and t < 20:
        C = []
        v = find_max_degree(S,G,th)
        C.append(v)
        S.remove(v)
        b,x = cercano(th,C,S,G)
 
        while b == 1:  
            C.append(x)
            S.remove(x)
            b,x = cercano(th,C,S,G)
        
        P.append(C)
        for node in C:
            G = G.drop(index=[node,node],columns=[node,node])     
        t += 1   
        
    print(P)
    
    return P

if __name__ == "__main__":
    G = pd.read_csv('file_1.csv',header=None)
    #th = promedio_umbral(G)
    th = 6
    algoritmo(G,th)