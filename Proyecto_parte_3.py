import os

def borrar_terminal (n=int(input("Digita un numero: "))):
    
    for i in range(0,n+1):
        letra = (input())
        if letra == 'n':
            os.system('cls' if os.name=='nt' else 'clear')
            print(i)


borrar_terminal()