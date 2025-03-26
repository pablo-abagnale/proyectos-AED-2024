class Agente:
    def __init__(self, legajo,documento,agente,mail,supervisor,cuenta):
        self.legajo = legajo  #Legajo OMNIA
        self.documento = documento #DNI sin puntos
        self.agente = agente # Nombre completo Apellido + Nombre
        self.mail = mail #Mail Naranja NX / Usuario Botmaker
        self.supervisor = supervisor #Equipo
        self.cuenta = cuenta #Sub campaña

    def __str__(self):
        return f'DNI: {self.documento:<10} Agente: {self.agente:<35} mail: {self.mail:<40} Equipo : {self.supervisor}'

class Control:
    def __init__(self,mail,agente,rol,cola,estado,fecha,time):
        self.mail = mail
        self.agente = agente
        self.rol = rol
        self.cola = cola
        self.estado = estado
        self.fecha = fecha
        self.time = time

    def __str__(self):
        return f'mail:{self.mail:<40} rol: {self.rol:<40} servicio: {self.cola:<17} estado: {self.estado:<15} fecha: {self.fecha:<15} duracion: {self.time:<5} horas'

class Utilizacion:
    def __init__(self,mail,agente,equipo,fecha,horas,disponible,no_disponible,descanso,ocupado,coaching,almuerzo):
        self.mail = mail
        self.agente = agente
        self.equipo = equipo
        self.fecha = fecha
        self.horas = horas
        self.disponible = disponible
        self.no_disponible = no_disponible
        self.descanso = descanso
        self.ocupado = ocupado
        self.coaching = coaching
        self.almuerzo = almuerzo

    def __str__(self):
        return f'Fecha: {self.fecha} Mail:{self.mail:<30} rol: {self.agente:<30} : {self.equipo:<30} Horas: {self.horas:<10} hs Aux: {self.no_disponible + self.descanso + self.ocupado:<15}'