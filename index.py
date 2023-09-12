#Take dates from  __init_.py
from Cliente import Cliente


# Clase Cliente desde modulo1
cliente1 = Cliente("Agustin", "Brunello", "agusitn@gmail.com", 1000)


print(cliente1)  # Imprime el nombre del cliente
print(cliente1.mostrar_informacion())  # Muestra toda la información del cliente
print(cliente1.realizar_compra(500))  # Realiza una compra





