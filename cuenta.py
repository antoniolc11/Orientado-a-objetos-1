class Cuenta:
    __numero = 0
    __cuentas = {}
    def __init__(self, titular, saldo):
        Cuenta.__numero += 1
        self.__numero = Cuenta.__numero
        self.__titular = titular
        self.__saldo = saldo
        self.__movimientos = []
        Cuenta.__cuentas[self.__numero] = self

    def numero(self):
        return self.__numero

    def titular(self):
        return self.__titular

    def movimientos(self):
        return self.__movimientos

    def saldo(self):
        return self.__saldo

    def __set_saldo(self, movimiento):
        if movimiento.concepto() == 'ingresar':
            self.__saldo += movimiento.cantidad()
        elif movimiento.concepto() == 'retirar':
            self.__saldo -= movimiento.cantidad()
        else:
            raise ValueError('El movimiento indicado no existe')

    def set_ayadir_movimiento(self, movimiento):
        self.__movimientos.append(movimiento)
        self.__set_saldo(movimiento)

    @staticmethod
    def cuenta(numero):
        return Cuenta.__cuentas[numero]
