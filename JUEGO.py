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

    def mostrar_palabra(self):
        mostrar = ""
        
        for letra in self.palabra:
            if letra in self.letras_encontradas:
                mostrar += letra + " "
            else:
                mostrar += "_ "
        
        print("\n" + mostrar)
    
    def conseguir_letra(self):
        while True:
            letra = input("ingresa una letra: ").lower()
            
            
            if len(letra) == 1 and letra.isalpha():
                return letra
            
            print("Por favor ingrese una sola letra.") 
    
    def probar_letra(self, letra):
        if letra in self.letras_palabras:
            self.letras_palabras.remove(letra)
            self.letras_encontradas.add(letra)
            print("Correcto!")
        else:
            self.vidas -= 1
            print("lo siento. Tienes", self.vidas, "vidas.")
            self.mostrar_adivina_adivinador()

    def mostrar_adivina_adivinador(self):
        casos = [
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
            """,
            """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
            """,
            """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
            """,
            """
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
            """,
            """
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
            """,
            """
                --------
                |      |
                |      
                |    
                |      
                |     
                -
            """
       ]
        print(casos[self.vidas])       