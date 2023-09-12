class Cliente:
    # Constructor de la clase
    def __init__(self, nombre, apellido, email, saldo):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.saldo = saldo

    # Método para mostrar la información del cliente
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre} {self.apellido}\nEmail: {self.email}\nSaldo: ${self.saldo}"

    # Método para realizar una compra
    def realizar_compra(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Compra realizada con éxito. Nuevo saldo: ${self.saldo}"
        else:
            return "Saldo insuficiente para realizar la compra."

    # Método str para representar el objeto como una cadena
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}"
    
    def changeName(self, newName): 
        self.nombre = newName
        print(self.nombre)

