from flask import Blueprint, request, jsonify

from controllers.GastoComunController import GastoComunController

gasto_comun_blueprint = Blueprint('gasto_comun_blueprint', __name__)

class GastoComunView:
    @staticmethod
    @gasto_comun_blueprint.route('/gasto_comun', methods=['GET'])
    def get_all_gasto_comun():
        gastos_comunes = GastoComunController.get_all_gasto_comun()
        
        return jsonify([gasto_comun.serialize() for gasto_comun in gastos_comunes])
    
    @staticmethod
    @gasto_comun_blueprint.route('/gasto_comun', methods=['POST'])
    def create_gasto_comun():
        data = request.json
        fecha_vencimiento = data.get('fecha_vencimiento')
        costo = data.get('costo')
        fecha_pago = data.get('fecha_pago')
        numero_departamento = data.get('numero_departamento')
        periodo = data.get('periodo')
        
        nuevo_gasto_comun = GastoComunController.create_gasto_comun(fecha_vencimiento, costo, fecha_pago, numero_departamento, periodo)
        
        return jsonify(nuevo_gasto_comun.serialize())
    
    @staticmethod
    @gasto_comun_blueprint.route('/gasto_comun/<int:gasto_comun_id>', methods=['PUT'])
    def registrar_pago(gasto_comun_id):
        gasto_comun = GastoComunController.registrar_pago(gasto_comun_id)
        
        return jsonify(gasto_comun.serialize())
    
    @staticmethod
    @gasto_comun_blueprint.route('/gasto_comun/pendientes/<int:numero_departamento>', methods=['GET'])
    def get_gastos_pendientes(numero_departamento):
        gastos_pendientes = GastoComunController.get_gastos_pendientes(numero_departamento)
        
        return jsonify([gasto_comun.serialize() for gasto_comun in gastos_pendientes])
    
    @staticmethod
    @gasto_comun_blueprint.route('/gasto_comun/pagados/<int:numero_departamento>', methods=['GET'])
    def get_gastos_pagados(numero_departamento):
        gastos_pagados = GastoComunController.get_gastos_pagados(numero_departamento)
        
        return jsonify([gasto_comun.serialize() for gasto_comun in gastos_pagados])