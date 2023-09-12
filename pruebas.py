# class Cliente:
#     # Constructor de la clase
#     def __init__(self, nombre, apellido, email, saldo):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.email = email
#         self.saldo = saldo

#     # Método para mostrar la información del cliente
#     def mostrar_informacion(self):
#         return f"Nombre: {self.nombre} {self.apellido}\nEmail: {self.email}\nSaldo: ${self.saldo}"

#     # Método para realizar una compra
#     def realizar_compra(self, cantidad):
#         if cantidad <= self.saldo:
#             self.saldo -= cantidad
#             return f"Compra realizada con éxito. Nuevo saldo: ${self.saldo}"
#         else:
#             return "Saldo insuficiente para realizar la compra."

#     # Método especial para representar el objeto como una cadena
#     def __str__(self):
#         return f"Cliente: {self.nombre} {self.apellido}"

# # Ejemplo de uso de la clase Cliente
# cliente1 = Cliente("Agustin", "Brunello", "agustin@gmail.com", 1000)
# print(cliente1)  # Imprime el nombre del cliente
# print(cliente1.mostrar_informacion())  # Muestra toda la información del cliente
# print(cliente1.realizar_compra(500))  # Intenta hacer una compra


#link para paquete redistribuible
#   pip install ruta/al/archivo/mi_paquete_redistribuible-0.1.tar.gz
