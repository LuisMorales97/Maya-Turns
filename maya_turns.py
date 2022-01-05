import time
import numpy as np
import sys

#Respuesta demorada

def imp_demora(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#Clase Principal

class Maya:
    def __init__(self, nombre, tipos, movimientos, evs, hp='=========='):
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = evs['ataque']
        self.defensa = evs['defensa']
        self.hp = hp
        self.barras = 20

    #Imprimir informacion Inicial#
    def datos_vs(self, Maya2):
        '''Imprimir info batalla'''
        print("===Batalla===")
        print(f"\n{self.nombre}")
        print("tipo/",self.tipos)
        print("ataque/",self.ataque)
        print("defensa/",self.defensa)
        print("Nv./",3*(1+np.mean([self.ataque,self.defensa])))
        print("\nVS")
        print(f"\n{Maya2.nombre}")
        print("tipo/", Maya2.tipos)
        print("ataque/",Maya2.ataque)
        print("defensa/",Maya2.defensa)
        print("Nv./",3*(1+np.mean([Maya2.ataque,Maya2.defensa])))
        time.sleep(2)

    #Define ventajas de tipos#
    def sup_tipo(self,Maya2):
        '''Ataque y defensa en los tipos'''
        version = ['Cielo', 'Tierra', 'Fuego']
        for i,k in enumerate(version):
            if self.tipos == k:
                if Maya2.tipos == k:
                    cadena_1_ataque = '\nNo es muy efectivo'
                    cadena_2_ataque = '\nNo es muy efectivo'
                if Maya2.tipos == version[(i+1)%3]:
                    Maya2.ataque *= 2
                    Maya2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /=2
                    cadena_1_ataque  = '\nNo es muy efectivo'
                    cadena_2_ataque = '\nEs muy efectivo'
                if Maya2.tipos == version[(i+1)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    Maya2.ataque /= 2
                    Maya2.defensa /=2
                    cadena_1_ataque  = '\nEs muy efectivo'
                    cadena_2_ataque = '\nNo es muy efectivo'
            return cadena_1_ataque, cadena_2_ataque
    
    #Realiza los turnos de cada oponente#
    def turnos(self, Maya2, cadena_1_ataque, cadena_2_ataque):
        while (self.barras > 0) and (Maya2.barras > 0):
            print(f"\n{self.nombre}\t\tPS\t{self.hp}")
            print(f"\n{Maya2.nombre}\t\tPS\t{Maya2.hp}")

            #Turno Maya#
            print(f"¡Adelante {self.nombre}!")
            for i,x in enumerate(self.movimientos):
                print(f"{i+1.}.", x)
            index = int(input('Elige el movimiento: '))
            imp_demora(f"\n¡{self.nombre} usó {self.movimientos[index-1]}!")
            time.sleep(1)
            imp_demora(cadena_1_ataque)

            Maya2.barras -= self.ataque
            Maya2.hp = ""

            for j in range(int(Maya2.barras+.1*Maya2.defensa)):
                Maya2.hp += "="
            
            time.sleep(1)
            print(f"\n{self.nombre}\t\tPS\t{self.hp}")
            print(f"\n{Maya2.nombre}\t\tPS\t{Maya2.hp}")
            time.sleep(5)

            if Maya2.barras <= 0:
                imp_demora("\n..." + Maya2.nombre + ' se debilitó.')

            #Turno Maya2#
            print(f"¡Adelante {Maya2.nombre}!")
            for i,x in enumerate(Maya2.movimientos):
                print(f"{i+1.}.", x)
            index = int(input('Elige el movimiento: '))
            imp_demora(f"\n¡{Maya2.nombre} usó {Maya2.movimientos[index-1]}!")
            time.sleep(1)
            imp_demora(cadena_2_ataque)

            Maya2.barras -= Maya2.ataque
            Maya2.hp = ""

            for j in range(int(self.barras+.1*self.defensa)):
                Maya2.hp += "="
            
            time.sleep(1)
            print(f"\n{self.nombre}\t\PS\t{self.hp}")
            print(f"\n{Maya2.nombre}\t\PS\t{Maya2.hp}")
            time.sleep(5)

            if Maya2.barras <= 0:
                imp_demora("\n..." + self.nombre + ' se debilitó.')
    
    #Inicializa las funciones declaradas empezando el enfrentamiento#
    def enfrentamiento(self, Maya2):
        self.datos_vs(Maya2)
        cadena_1_ataque, cadena_2_ataque = self.sup_tipo(Maya2)
        self.turnos(Maya2, cadena_1_ataque, cadena_2_ataque)
        mp = np.random.choice(5000)
        imp_demora(f"\nEl oponente te pagó ${mp}.\n")

if __name__ == '__main__':
    Kukulkan = Maya('Kukulkan', 'Cielo', ['Ataque Solar', 'Regeneracion', 'Aterrizage', 'Llamarada'], {'ataque':12, 'defensa': 8})
    Balam = Maya('Balam', 'Tierra', ['Garra', 'Mirada Furtiva', 'Colmillo', 'Segador'], {'ataque':10, 'defensa': 10})
    Itzamna = Maya('Itzanma', 'Fuego', ['Energia Solar', 'Medicina Absoluta', 'Gravedad Aplastante', 'Grieta'], {'ataque':8, 'defensa': 12})
    #Se definen los adversarios#
    Kukulkan.enfrentamiento(Balam)
