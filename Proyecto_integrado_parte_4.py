import os
from readchar import readkey, key
from colorama import Fore, Back, Style, init


Laberinto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

def cambiar_caracteres_a_matriz(cadena:str):
    return cadena.split('\n')

Matriz_Laberinto=cambiar_caracteres_a_matriz(Laberinto)

mapa_matriz = [list(palabra) for palabra in Matriz_Laberinto]


def imprimir(mapa):
    os.system('cls' if os.name=='nt' else 'clear') 
    matriz = []
    for i in mapa:
        conca =''.join(i)
        matriz.append(conca)
   
    for i in matriz:
        print (i)  

def main_loop (mapa_matriz):
    coor_px = 0
    coor_py = 0
    Nombre_Usuario = input("Digta tu nombre: ")
    print(Style.BRIGHT + Fore.BLUE + Nombre_Usuario + Style.RESET_ALL)
    init()
    while True:
        if coor_px == len(mapa_matriz)-1 and coor_py == len(mapa_matriz[0])-2:
             
             print(f'Felicidades {Nombre_Usuario} has ganado')
             break

        else:   
                       
                mapa_matriz [coor_px][coor_py] = Nombre_Usuario[0]
                imprimir(mapa_matriz)
                    
                k = readkey()
                    #Arriba
                if coor_px-1 >= 0 and mapa_matriz [coor_px-1][coor_py] != '#' and k==key.UP:             
                            if k  == key.UP:
                                coor_px -= 1
                                mapa_matriz [coor_px+1][coor_py] = '.'
                                mapa_matriz [coor_px][coor_py] = Nombre_Usuario[0]
                                imprimir(mapa_matriz)
                                k = None
                    #Abajo
                elif coor_px + 1 <= len(mapa_matriz[0])-1 and mapa_matriz [coor_px+1][coor_py] != '#' and k == key.DOWN:       
                            coor_px += 1
                            if k  == key.DOWN:
                                mapa_matriz [coor_px-1][coor_py] = '.'
                                mapa_matriz [coor_px][coor_py] = Nombre_Usuario[0]
                                imprimir(mapa_matriz)
                                k = None 
                    #Derecha
                elif coor_py + 1 >= 0 and mapa_matriz[coor_px][coor_py + 1] != '#'and k == key.RIGHT :             
                            coor_py += 1
                            if k  == key.RIGHT:
                                mapa_matriz [coor_px][coor_py - 1] = '.'
                                mapa_matriz [coor_px][coor_py] = Nombre_Usuario[0]
                                imprimir(mapa_matriz)
                                k = None
                elif coor_py - 1 >=0 and mapa_matriz[coor_px][coor_py - 1] != '#'and k == key.LEFT :             
                            coor_py -= 1
                            if k  == key.LEFT:
                                mapa_matriz [coor_px][coor_py + 1] = '.'
                                mapa_matriz [coor_px][coor_py] = Nombre_Usuario[0]
                                imprimir(mapa_matriz)
                                k = None                         
                

main_loop(mapa_matriz)
  
            

       
                
    
            

           
        
            
            
            
       
           


         



