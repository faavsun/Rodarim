from app import db

class GastoComunModel(db.Model):
    __tablename__ = 'gasto_comun'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
    costo = db.Column(db.Float, nullable=False)
    fecha_pago = db.Column(db.Date, nullable=True)
    numero_departamento = db.Column(db.Integer, db.ForeignKey('departamento.numero'), nullable=False)
    periodo = db.Column(db.Date, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "fecha_vencimiento": self.fecha_vencimiento,
            "costo": self.costo,
            "fecha_pago": self.fecha_pago,
            "numero_departamento": self.numero_departamento,
            "periodo": self.periodo
        }