def cifrar_cesar(texto, llave):
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            ascii_base = 65 if caracter.isupper() else 97
            codigo_cifrado = (ord(caracter) - ascii_base + llave) % 26 + ascii_base
            resultado += chr(codigo_cifrado)
            
        else:
            resultado += caracter
    
    return resultado

def descifrar_cesar(texto_cifrado, llave):
    return cifrar_cesar(texto_cifrado, -llave)

def run():
    while True:
        print("1. Cifrar un mensaje")
        print("2. Descifrar un mensaje")
        print("3. Salir")
        opcion = int(input("\nSeleccione una opción: "))
        
        if opcion == 1:
            mensaje = input("\nIngrese el mensaje a cifrar: ")
            
            while True:
                try:
                    llave = int(input("Ingrese la llave numérica (número entero): "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
            
            mensaje_cifrado = cifrar_cesar(mensaje, llave)
            print(f"\nMensaje cifrado: {mensaje_cifrado}\n")
            
        elif opcion == 2:
            mensaje_cifrado = input("\nIngrese el mensaje cifrado: ")
            
            while True:
                try:
                    llave = int(input("Ingrese la llave numérica utilizada para cifrar: "))
                    break
                except ValueError:
                    print("Error: Debe ingresar un número entero.")
            
            mensaje_descifrado = descifrar_cesar(mensaje_cifrado, llave)
            print(f"\nMensaje descifrado: {mensaje_descifrado}\n")
            
        elif opcion == 3:
            print("\nSaliendo del programa...\n")
            break
            
        else:
            print("\nOpción no válida")

if __name__ == "__main__":
    run()
