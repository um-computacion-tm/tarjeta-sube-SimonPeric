class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

PRIMARIO = "primario"
SECUNDARIO = "secundario"
UNIVERSITARIO = "universitario"
JUBILADO = "jubilado"
ACTIVADO = "activado"
DESACTIVADO = "desactivado"
PRECIO_TICKET = 70

DESCUENTOS = {
    PRIMARIO: 50,
    SECUNDARIO: 40,
    UNIVERSITARIO: 30,
    JUBILADO: 25,
}


class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = "activado"

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == None:
            return PRECIO_TICKET
        elif self.grupo_beneficiario == PRIMARIO:
            return PRECIO_TICKET * 0.5
        elif self.grupo_beneficiario == SECUNDARIO:
            return PRECIO_TICKET * 0.6
        elif self.grupo_beneficiario == UNIVERSITARIO:
            return PRECIO_TICKET * 0.7 
        elif self.grupo_beneficiario == JUBILADO:
            return PRECIO_TICKET * 0.75
        
    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException()
        elif self.saldo < self.obtener_precio_ticket() :
            raise NoHaySaldoException()
        elif self.grupo_beneficiario == PRIMARIO or SECUNDARIO or UNIVERSITARIO or JUBILADO and self.estado == ACTIVADO:
            self.saldo -= self.obtener_precio_ticket()
            return self.saldo
        
    def cambiar_estado(self,estado):
        validos = [ACTIVADO, DESACTIVADO]
        if not estado in validos:
            raise EstadoNoExistenteException()
        self.estado = estado