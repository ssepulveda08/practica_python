import random

WELCOME =  """
------------------------------------------------------------------------------------------
         ____   ____    ___  ____   __ __    ___  ____   ____  ___     ___  
        |    \ l    j  /  _]|    \ |  T  |  /  _]|    \ l    j|   \   /   \ 
        |  o  ) |  T  /  [_ |  _  Y|  |  | /  [_ |  _  Y |  T |    \ Y     Y
        |     T |  | Y    _]|  |  ||  |  |Y    _]|  |  | |  | |  D  Y|  O  |
        |  O  | |  | |   [_ |  |  |l  :  !|   [_ |  |  | |  | |     ||     |
        |     | j  l |     T|  |  | \   / |     T|  |  | j  l |     |l     !
        l_____j|____jl_____jl__j__j  \_/  l_____jl__j__j|____jl_____j \___/ 
    
Listo para jugar 
1. Iniciar
2. Cerrar 
------------------------------------------------------------------------------------------
    """
    

def game_completed(ramdom):
    try: 
        myValue = int(input("Elige un Numero del 1 al 100: " ))
        if(myValue == ramdom): 
            print("Felicitaciones !Ganaste¡")
            return True
        else:
            if(myValue > ramdom):
                print("El numero es mas pequeño")
                return False  
            else:
                print("el numero es mas Grande")
                return False     

    except ValueError:
        print("Dato Invalido")
        return False    
               

def start_game():
    value = random.randrange(100)
    if_number_found = False
    while if_number_found != True:
        if_number_found = game_completed(value)

    init_main()


def init_main():
    option = input(WELCOME)
    if option == "1":
        start_game()
    elif option == "2":
        exit()
    else: 
        print("Opcion no valida") 

     

def main ():  
    init_main()

if __name__ == "__main__":
    main()    