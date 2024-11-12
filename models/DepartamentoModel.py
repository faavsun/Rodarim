from app import db

class DepartamentoModel(db.Model):
    __tablename__ = 'departamento'
    
    numero = db.Column(db.Integer, primary_key=True)
    rut_residente = db.Column(db.String(10), nullable=False)
    rut_propietario = db.Column(db.String(10), nullable=True)
    id_tipo_dpto = db.Column(db.Integer, nullable=False)
    
    gastos_comunes = db.relationship('GastoComunModel', backref='departamento', lazy=True)
    
    def serialize(self):
        return {
            "numero": self.numero,
            "rut_residente": self.rut_residente,
            "rut_propietario": self.rut_propietario,
            "id_tipo_dpto": self.id_tipo_dpto
        }