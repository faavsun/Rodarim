from services.GastoComunService import GastoComunService

class GastoComunController:
    @staticmethod
    def get_all_gasto_comun():
        return GastoComunService.get_all_gasto_comun()
    
    @staticmethod
    def create_gasto_comun(fecha_vencimiento, costo, fecha_pago, numero_departamento, periodo):
        return GastoComunService.create_gasto_comun(fecha_vencimiento, costo, fecha_pago, numero_departamento, periodo)
    
    @staticmethod
    def get_gasto_comun_by_id(gasto_comun_id):
        return GastoComunService.get_gasto_comun_by_id(gasto_comun_id)
    
    @staticmethod
    def registrar_pago(gasto_comun_id):
        return GastoComunService.registrar_pago(gasto_comun_id)

    @staticmethod
    def get_gastos_pendientes(numero_departamento):
        return GastoComunService.get_gastos_pendientes(numero_departamento)
    
    @staticmethod
    def get_gastos_pagados(numero_departamento):
        return GastoComunService.get_gastos_pagados(numero_departamento)