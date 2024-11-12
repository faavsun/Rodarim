from models.GastoComunModel import db, GastoComunModel
from datetime import datetime

class GastoComunService:
    @staticmethod
    def get_all_gasto_comun():
        return GastoComunModel.query.all()
    
    @staticmethod
    def create_gasto_comun(fecha_vencimiento, costo, fecha_pago, numero_departamento, periodo):
        fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d').date() if fecha_vencimiento else None
        fecha_pago = datetime.strptime(fecha_pago, '%Y-%m-%d').date() if fecha_pago else None
        periodo = datetime.strptime(periodo, '%Y-%m').date() if periodo else None

        nuevo_gasto = GastoComunModel(
            fecha_vencimiento=fecha_vencimiento,
            costo=costo,
            fecha_pago=fecha_pago,
            numero_departamento=numero_departamento,
            periodo=periodo
        )
        
        db.session.add(nuevo_gasto)
        db.session.commit()
        
        return nuevo_gasto
    
    @staticmethod
    def registrar_pago(gasto_comun_id):
        gasto = GastoComunModel.query.get(gasto_comun_id)
        gasto.fecha_pago = datetime.now()
        
        db.session.commit()
        
        return gasto
    
    @staticmethod
    def get_gastos_pagados(numero_departamento):
        return GastoComunModel.query.filter_by(numero_departamento=numero_departamento).filter(GastoComunModel.fecha_pago.isnot(None)).all()
    
    @staticmethod
    def get_gastos_pendientes(numero_departamento):
        return GastoComunModel.query.filter_by(numero_departamento=numero_departamento).filter(GastoComunModel.fecha_pago.is_(None)).all()