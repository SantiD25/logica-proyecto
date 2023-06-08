print("este es el archivo para el juego")
import random

class Adivina_adivinador:
    def __init__(self):
        self.palabras = ["manzana", "pera", "mango","piña", "poma", "ceresa", "coco", "kiwi", "limon", "banano", "maracuya", "mora", "sandia", "uva", "ciruela", "fresa", "papaya", "mandarina", "naranja", "lulo", "guanabana", "mamoncillo", "guayaba", "maracuya", "melocoton"]
        self.palabra = random.choice(self.palabras)
        self.letras_palabras = set(self.palabra)
        self.letras_encontradas = set()
        self.vidas = 6
        
        #self.jugar()
    
    def jugar(self):
        print("BIENVENIDO A ADIVINA_ADIVINADOR!")
        print("adivina la futa")
        
        while self.vidas > 0 and self.letras_palabras:
            self.mostrar_palabra()
            letra = self.conseguir_letra()
            self.probar_letra(letra)
        
        if self.letras_palabras:
            print("Perdiste la palabra era:", self.palabra)
        else:
            print("¡Felicidades adivinaste! la palabra:", self.palabra)