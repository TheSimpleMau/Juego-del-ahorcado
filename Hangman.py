##############################
######By Mauricio Olguín######
##############################


##############################
######Modulos a importar######
##############################

from getpass import getuser #Para obtener el nombre del usuario
from HangmanPics import hangmanpic, WIN #Importamos de otro archivo ciertas figuras
from TutorialHangman import tutorial, waiting #La primera función es para el tutorial, es segundo es para dar "tiempos de carga"
from cowsay import tux #Para poner a Tux (la mascota de Linux)
import random #Para escoger nuestra palabra al azar


###############################################
######Definiendo todas nuestras funciones######
###############################################

#Función para convertir una palabra en una lista
def split(palabra):
    return [char for char in palabra]


#Función para remplazar una lista con la letra que buscamos de la palabra orginal
def replaceword(OG_word:list,making_word:str,letter:str)->list:
    new_word = list(making_word)
    counter = 0
    for letra in OG_word:
        if letter == letra:
            new_word[counter] = letter
        elif letter != letra:
            pass
        counter+=1
    return new_word

#Función para buscar la vocales que hay dentro de una palabra
def vocales(word:list)->list:
    i=0
    vocales = []
    vowls = ['A','E','I','O','U']
    for letter in word:
        if letter in vowls:
            if letter in vocales:
                pass
            else:
                i+=1
                vocales.append(letter)
    return i,vocales

#Función para añandir una coma para despues hacer la lista de las letras que llevamos
def addcoma(letra:list)->list:
    exaple = []
    if letra == exaple:
        return letra
    else:
        letra += ','
        return letra

#Función para concatenar una lista llena de caracteres
def join_list(lista:list)->list:
    lista = "".join(lista)
    return lista

#Generando un diccionario con todas las palabras que se encuentran dentro
#de nuestro archivo "data.txt" con todas las palabras
words = {}
with open("data.txt","r",encoding="utf-8") as f:
    for word in f:
        word = word.upper()
        letters = split(word)
        if '\n' in word:
            letters = letters[:-1]
            word = join_list(letters)
        words.update({f'{word}':letters})

#Función para seleccionar una palabra dentro del diccionario 'words' y jugar con esa palabra.
def random_word()->list:
    makeing_list = list(words.items())
    random_choice = random.choice(makeing_list)
    return random_choice

#Función para escoger el modo de juego
def modo()->list:
    waiting(0,True)
    tux('Antes de empezar a jugar, escoge entre los siguiente modos de juego...')
    print('''     -Fácil-      -Intermedio-     -Difícil-
        
        Escribe F, I o D para seleccionar.''')
    try:
        mode = str(input('      Mi modo de juego será: ')).lower()
    except AssertionError:
        print('Error, escribe unicamente F para fácil, I para intermedio y D para difícil (tampoco costaba tando deducirlo :/)')
        modo()
    if mode == 'f':
        return hangmanpic,'f',6
    elif mode == 'i':
        HANGMANPICS = list(map(hangmanpic.__getitem__, (0,2,4,5,6)))
        return HANGMANPICS,'i',4
    elif mode == 'd':
        HANGMANPICS = list(map(hangmanpic.__getitem__, (0,3,6)))
        return HANGMANPICS,'d',2


#Pequeña bienvenida al juego
def introducction()->None:
    username = getuser().capitalize()
    waiting(0,True)
    try:
        tux(f'Bienvenido {username}')
        waiting(5,True)
        tux(f'En esta ocación, vamos a jugar al juego del ahorcado')
        waiting(5,True)
    except KeyboardInterrupt:
        pass
    waiting(0,True)
    tux(f'Sabes como jugarlo?')
    print('''       Si se como jugar = S
No se como jugar = N''')
    try:
        jugar = str(input('     La verdad es que... ')).lower()
        assert jugar == 's' or jugar == 'n'
    except AssertionError:
        print('No se que escribiste, pero definitivamente no lo que te dije que hiciera, así que asumiré que si sabes jugar...')
        waiting(3,False)
        jugar = 's'
    if jugar == 's':
        print('Genial!!! Entonces vamos a hecharnos una partida')
        waiting(7,True)
    else:
        tutorial()

#Función donde sucede el juego
def game()->bool:
    player_mode = modo()
    #Número de vocales por si es que el modo lo permite
    try:
        if 'f' in player_mode or 'i' in player_mode:
            pista = True
        else:
            pista = False
    except TypeError:
        print('Error, escriba solo F para fácil, I para intermedio o D para difícil')
        exit()
    
    # Selección de la palabra aleatoria y otros arreglos
    no_attempts = player_mode[2]
    attempt = 0
    word_playing = random_word()
    len_word= len(word_playing[1])
    user_try_word = [' _ ']*len_word
    letters_used = []

    # Inicio del juego
    waiting(0,True)
    while no_attempts >= attempt:
        print(f'''
        {player_mode[0][attempt]}

            {join_list(user_try_word)}

    Tienes {no_attempts} intentos y has usado {attempt}
    Has usado las letras: {join_list(addcoma(letters_used))}

''')
        # Si pista exsite
        if pista == True:
            no_vowls = vocales(word_playing[1])
            print(f'    Pssst, en la palabra hay {no_vowls[0]} vocales\n')
        else:
            pass
        # Obteniendo la letra del usuario
        user_letter = str(input('       Escibe una letra: ')).upper()
        # if len(user_letter) > 1:
        #     print('     Escribe unicamente una letra por jugada.')
        # Marcar que letras hemos usados
        letters_used.append(user_letter)
        # Revision despues de la palabra con la palabra formada del usuario
        check_after = list(user_try_word)
        # Remplazo de letras correctas
        user_try_word = replaceword(word_playing[1],user_try_word,user_letter)
        ### Condiciones para puntaje:
        #Si la palabra formada por usuario no ha cambiado con respecto a la variable check_after
        if user_try_word == check_after:
            attempt+=1
            if attempt != no_attempts:
                wait = input('''    Esa letra no está, presione enter para continuar ''')
                pass
            elif attempt == no_attempts:
                waiting(0,True)
                print(player_mode[0][attempt])
                print(f'Has perdido, la palabra que estaba buscando era {word_playing[0]}')
                again = str(input('Quieres volver a jugar? (Escribe S o N) ')).lower()
                if again == 's':
                    return True
                else:
                    return False
        #Si la palabra cambio con check_after
        elif user_try_word != check_after:
            if user_try_word == word_playing[1]:
                waiting(0,True)
                print(f'''        {WIN}
           Has gando!!!
    La palabra es {join_list(user_try_word)}''')
                try:
                    again = str(input('Quieres volver a jugar? (Escribe S o N) ')).lower()
                    assert(again == 's' or again == 'n')
                except AssertionError:
                    print('Escribe solo S para sí y N para no. De todas formas, vamos a jugar de nuevo.')
                    waiting(5,False)
                    return True
                if again == 's':
                    return True
                elif again == 'n':
                    return False
                elif again == '':
                    print('Escribe solo S para sí y N para no. De todas formas, vamos a jugar de nuevo.')
                    waiting(5,False)
                    return True
            else:
                pass
        waiting(0,True)

#Función principal, aquí simplemente enseñamos la introducción y encerramos la función
#'game' en un ciclo while para jugar hasta que el usuario decida
def main()->None:
    introducction()
    again = None
    while again != False:
        again = game()
    tux('Como dijo mi ex, hasta aquí llegamos. Gracias por jugar!!!')
    waiting(6,True)
    

#Entry point
if __name__ == '__main__':
    main()