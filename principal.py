from cliente import Cliente
from movimiento import Movimiento
from cuenta import Cuenta

cliente1 = Cliente('47344703P', 'Antonio', 'Martinez')
cuenta1 = Cuenta(cliente1, 100)
cuenta2 = Cuenta(cliente1, 200)

cuenta1.set_ayadir_movimiento(Movimiento('ingresar', 50))
cuenta1.set_ayadir_movimiento(Movimiento('ingresar', 200))
cuenta1.set_ayadir_movimiento(Movimiento('retirar', 100))
print(cuenta1.saldo())

cuenta2.set_ayadir_movimiento(Movimiento('ingresar', 200))
cuenta2.set_ayadir_movimiento(Movimiento('ingresar', 200))
cuenta2.set_ayadir_movimiento(Movimiento('retirar', 100))
print(cuenta2.saldo())
print(cuenta1.movimientos())
