import math

def is_prime(number):
    counter = 0
    square = math.sqrt(number)
    val = int(square)
    for i in range(1, val + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1  
    return counter == 0 and number != 0 and number != 1 

    

def main():
    number = int(input("Escribe un núumero: "))
    if(is_prime(number)):
        print("Es primno")
    else:
        print("No es primo")    



if __name__ == "__main__":
    main()  