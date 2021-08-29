from os import system
from time import sleep
from cowsay import tux
from HangmanPics import hangmanpic, WIN

def waiting(tiempo:float,clear:bool)->None:
    sleep(tiempo)
    if clear == True:
        system('clear')
    else:
        pass

def tutorial()->None:
    system('clear')
    tux('El juego del ahorcado es muy sencillo de jugar')
    waiting(5,True)
    tux('Tendrás que adivinar una palabra, y la única información que tienes es cuantas letras hay en esta')
    waiting(7,True)
    tux('Veamos un ejemplo sencillo')
    waiting(5,True)
    print(f'''      Esta es la horca, ahora no hay nadie, pero
    si te equivocas de palabra, la iras pagando
    muy caro...
        {hangmanpic[0]}

                _ _ _ _     #En estos guiones bajos, iran apareciendo las letras
                            #a las cuales les vayas atinando de la palabra.
        
    En todos los modos de juego, te apoyaré con las palabras que
    Haz utilizado, pero si selecciónas el modo de juego fácil o 
    intermedio, te diré cuantas vocales hay dentro de la palabra,
    la diferencia entre uno y otro, es la cantidad de intentos.

''')
    stop = input('Presiona Enter para continuar...')
    system('clear')
    print(f'''  Pongamos de ejemplo que, la palabra que buscamos es "CASA" en el modo intermedio y es nuestro primer intento.
    Entonces, si escribimos "A", el juego quedaría de la siguiente manera:

        {hangmanpic[0]}

                _ A _ A

        Tienes 4 intentos y has usado 0
        Has usado las letras: A
        
        Psst, en la palabra hay 1 vocal

            Escribe una letra: (aquí podriamos nuestra siguiente letra)

    Fácil hasta ahora, verdad?
''')
    stop = input('Presiona Enter para continuar...')
    system('clear')
    print(f'''      Ahora, pongamonos en el caso de que ponemos mal una palabra, entonces, 
    ahora el juego se vería de la siguiente manera:

        {hangmanpic[0]}

                _ A _ A

        Tienes 4 intentos y has usado 1
        Has usado las letras: A,
        
        Psst, en la palabra hay 1 vocal
            Escribe una letra: X
            Esa palabra no esta, presione Enter para continuar 
        #Y entonces, al dar enter..
        

''')
    stop = input('Presiona Enter para continuar...')
    system('clear')
    print(f'''   Mientras más letras malas tengamos, más avanzará la figura del ahorcado.

        {hangmanpic[2]}

                _ A _ A

        Tienes 4 intentos y has usado 2
        Has usado las letras: A,X
        
        Psst, en la palabra hay 1 vocal
            Escribe una letra: (aquí podriamos nuestra siguiente letra)
    
    Por último, veamos como sería si estuviesemos jugando con una "animación"
''')
    stop = input('Presiona Enter para continuar...')
    system('clear')
    print(f'''
        {hangmanpic[0]}

            _ _ _ _ _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: 
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[0]}

            _ _ _ _ _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: 
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: A
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[0]}

            _ A _ _ _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[0]}

            _ A _ _ _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: i
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[0]}

            _ A _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[0]}

            _ A _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: R
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[0]}

            _ A _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: R
        Esa letra no está, presione enter para continuar 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            _ A _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            _ A _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: L
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            LA _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,L,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            LA _ I _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,L,
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: P
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            LAPI _
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,L,P
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: 
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            LAPI _ 
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,L,P
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: Z
    ''')
    waiting(3,True)
    print(f'''
        {hangmanpic[2]}

            LAPI _ 
        
        Tienes 4 intentos y has usado 2
        Has usado las letras: A,I,R,L,P
        
        Psst, en la palabra hay 2 vocal
            Escribe una letra: Z
    ''')
    waiting(3,True)
    print(f'''        {WIN}
           Has gando!!!
        La palabra es LAPIZ''')
    waiting(4,True)
    tux('Qué tal la animación eh?. Bueno, no importa')
    waiting(5,True)
    tux('Ahora que ya sabes jugar, vamos a escoger el modo de juego')
    waiting(7,True)

if __name__ == '__main__':
    pass