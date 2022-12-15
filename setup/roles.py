from rolepermissions.roles import AbstractUserRole

class Tecnico(AbstractUserRole):
    available_permissions = {
        'cadastrar' : True,
    }

class Controlador (AbstractUserRole):
    available_permissions = {
        'reportar_pane' : True,
    }

class Chefe (AbstractUserRole):
    available_permissions = {
        'visualizar_historico' : True,
    }

class Comandante (AbstractUserRole):
    available_permissions = {
        'abrir_fatd' : True,
    }