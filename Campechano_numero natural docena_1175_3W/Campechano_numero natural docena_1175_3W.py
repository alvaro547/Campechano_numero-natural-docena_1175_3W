print(" ")
print("Alvaro Campechano 3W")
print(" ")
def es_numero_natural(numero):
    """
    Verifica si el número es un número natural.

    Parámetros:
    numero (int): El número a verificar.

    Retorna:
    bool: True si es un número natural, False de lo contrario.
    """
    return isinstance(numero, int) and numero > 0

def main():
    """
    Función principal que solicita un número natural al usuario
    y verifica si está entre 1 y 12.
    """
    # Solicitar al usuario un número natural
    try:
        numero = int(input("Ingresa un número natural: "))
        
        # Verificar si el número es un número natural
        if not es_numero_natural(numero):
            print("Por favor, ingresa un número natural válido.")
            return
        
        # Verificar si el número está en la primera docena
        if 1 <= numero <= 12:
            print(f"El número {numero} está dentro de la primera docena.")
        else:
            print(f"El número {numero} no está dentro de la primera docena.")
    
    except ValueError:
        print("Entrada no válida. Asegúrate de ingresar un número natural.")

# Ejecutar la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
