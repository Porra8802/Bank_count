"""
Esta aplicación nos permite realizar la interacción entre cliente y banco respecto a las consultas de saldo, retiro y depositos y al finalizar
obtener los valores de los estados actuales de sus cuentas

"""

"Esta clase nos permite establecer las variables para utilizar posteriormente"
class Cuenta:

    def __init__(self, nombre, balance, balance_min) -> None:
        self.nombre=nombre
        self.balance=balance
        self.balance_min=balance_min

    def deposito(self, monto):
        self.balance += monto

    def retiro (self, monto):
        if (self.balance - monto >= self.balance_min and self.balance - monto>=0):
            self.balance-=monto

        else:
            print("No tienes fondos suficientes")

    def consulta_saldo(self):
        print(f"El saldo actual de la cuenta es ${self.balance} COP")

"Esta clase nos permite hacer los movimientos con la cuenta corriente de cada titular"
class Corriente(Cuenta):
    def __init__(self, nombre, balance) -> None:
        super().__init__(nombre, balance, balance_min = 0)

    def __str__(self) -> str:
        return f"La cuenta corriente a nombre de {self.nombre} tiene un saldo de ${self.balance} COP"

"Esta clase nos permite realizar los movimientos con la cuenta de ahorro de cada titular "
class Ahorro(Cuenta):
    def __init__(self, nombre, balance) -> None:
        super().__init__(nombre, balance, balance_min=0)

    def __str__(self) -> str:
        return f"La cuenta de ahorro a nombre de {self.nombre} tiene un saldo de ${self.balance} COP"

if __name__=="__main__":
    seleccion_servicio=int(input("Por favor ingrese el tipo de operación que desea realizar(1-Depositar, 2-Retirar, 3-Consultar saldo, 4-Salir): "))       
    
    while seleccion_servicio<=4 and seleccion_servicio>=1:   

        if seleccion_servicio==4:
            print("¡Gracias por utilizar nuestra aplicación!")
            break 
    
        tipo_cuenta=int(input("Por favor ingrese el tipo de cuenta(1-Ahorro, 2-Corriente): "))
        nombre=str(input("Ingrese el nombre del titular de la cuenta "))
        monto=int(input("Ingrese el valor del monto en COP "))
            
        if seleccion_servicio==1 and tipo_cuenta==1:
            ahorro=Ahorro(nombre, monto)
            print(ahorro)

        elif seleccion_servicio==1 and tipo_cuenta==2:
            corriente=Corriente(nombre, monto)
            print(corriente)
            break

        elif seleccion_servicio==2 and tipo_cuenta==1:
            ahorro=Ahorro(nombre, monto)
            ahorro.retiro(monto)
            print(ahorro.consulta_saldo())
            break

        elif seleccion_servicio==2 and tipo_cuenta==2:
            corriente=Corriente(nombre, monto)
            corriente.retiro(monto)
            print(corriente.consulta_saldo())
            break

        elif seleccion_servicio==3 and tipo_cuenta==1:
            corriente=Corriente(nombre, monto)
            corriente.consulta_saldo()
            break

        elif seleccion_servicio==3 and tipo_cuenta==2:
            corriente=Corriente(nombre, monto)
            corriente.consulta_saldo()
            break
        
        else:
            print("Estás solicitando una operación no encontrada por favor ingresa una operación adecuada")
            break





