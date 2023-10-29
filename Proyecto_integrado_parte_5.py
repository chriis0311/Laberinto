import random
import os
from readchar import readkey, key

class juego:
    def __init__(self, mapa, posi: int, posf: int,coor_x,coor_y):
        self.pos_i = posi
        self.pos_f = posf
        self.map = mapa
        self.coor_px = coor_x
        self.coor_py = coor_y
    #gets         
    def obtener_mapa(self):
        return self.map
    def obtener_posi(self):
        return self.pos_i
    def obtener_posf(self):
        return self.pos_f          
    #Metodos del juego
    def cambiar_caracteres_a_matriz(self,map):
        mapa_matriz = [list(palabra) for palabra in map]
        return mapa_matriz

    def imprimir(self,map):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"X : {self.coor_px}  Y : {self.coor_py}")
        matriz = []
        for i in map:
            conca = "".join(i)
            matriz.append(conca)

        for i in matriz:
            print(i)

    def main_loop(self,mapa_matriz):
        self.coor_px = int(self.pos_i[0])
        self.coor_py = int(self.pos_i[1])

        Nombre_Usuario = input("Digta tu nombre: ")
        print(type(self.coor_px))
        while True:
            
            if self.coor_py == int(self.pos_f[0]) and self.coor_px == int(self.pos_f[1]):
                mapa_matriz[self.coor_px][self.coor_py] = '.'
                
                self.imprimir(mapa_matriz)
                
                print(f"!Felicidades {Nombre_Usuario} has ganado¡")
                break
            
            else:
                mapa_matriz[self.coor_px][self.coor_py] = Nombre_Usuario[0]
                self.imprimir(mapa_matriz)
                k = readkey()
                if k == 'q':
                    print(f"Lamento que te tengas que ir {Nombre_Usuario} :(")
                    break
                # Arriba
                elif (self.coor_px - 1 >= 0 and mapa_matriz[self.coor_px - 1][self.coor_py] != "#" and k == key.UP):                  
                        self.coor_px -= 1
                        mapa_matriz[self.coor_px + 1][self.coor_py] = "."
                        mapa_matriz[self.coor_px][self.coor_py] = Nombre_Usuario[0]
                        self.imprimir(mapa_matriz)
                        k = None
                
                # Abajo
                elif (self.coor_px + 1 <= len(mapa_matriz[0]) - 1 and mapa_matriz[self.coor_px + 1][self.coor_py] != "#" and k == key.DOWN):
                        self.coor_px += 1
                        mapa_matriz[self.coor_px - 1][self.coor_py] = "."
                        mapa_matriz[self.coor_px][self.coor_py] = Nombre_Usuario[0]
                        self.imprimir(mapa_matriz)
                        k = None
                
                # Derecha
                elif (self.coor_py + 1 >= 0 and mapa_matriz[self.coor_px][self.coor_py + 1] != "#" and k == key.RIGHT):
                        self.coor_py += 1
                        mapa_matriz[self.coor_px][self.coor_py - 1] = "."
                        mapa_matriz[self.coor_px][self.coor_py] = Nombre_Usuario[0]
                        self.imprimir(mapa_matriz)
                        k = None
                
                #Izquierda
                elif (self.coor_py - 1 >= 0 and mapa_matriz[self.coor_px][self.coor_py - 1] != "#"and k == key.LEFT):
                        self.coor_py -= 1
                        mapa_matriz[self.coor_px][self.coor_py + 1] = "."
                        mapa_matriz[self.coor_px][self.coor_py] = Nombre_Usuario[0]
                        self.imprimir(mapa_matriz)
                        k = None

class juego_archivo(juego):
        def __init__(self,dir):
            self.ruta = dir 

        #Get ruta
        def obtener_ruta(self):
            return self.ruta    
          
        #leer el archivo   
        def leer_mapa (self,ruta:str):
            #Seleccionar mapa Aleatorio
            sel_mapa = os.listdir(ruta)
            mapa_aleatorio = random.choice(sel_mapa)
            with open(os.path.join(ruta, mapa_aleatorio), "r") as archivo:
                leer_pocisiones = archivo.readline().split(" ")
                leer_pocisiones[3] = leer_pocisiones[3].rstrip('\n') 
                
                #Posicion inicial posicion final
                self.pos_i = leer_pocisiones[:len(leer_pocisiones) // 2 ]
                self.pos_f = leer_pocisiones[len(leer_pocisiones) // 2:]
                
                leer_mapa = archivo.readlines()[0:]
                new_map = []
                for i in leer_mapa:
                    new_map.append(i.rstrip("\n"))
                self.map = new_map  
        
def main(ruta = input("Digita la ruta de los mapas: ")):
    Prueba1 = juego_archivo(ruta)
    Prueba1.leer_mapa(Prueba1.obtener_ruta())
    Prueba1.main_loop(Prueba1.cambiar_caracteres_a_matriz(Prueba1.obtener_mapa()))

main()




