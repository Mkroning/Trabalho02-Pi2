from sql_alchemy import banco

class VeiculoModel(banco.Model):
  __tablename__ = 'veiculos'

  veiculo_id = banco.Column(banco.Integer, primary_key=True)
  modelo = banco.Column(banco.String(50))
  placa = banco.Column(banco.String(15))
  marca = banco.Column(banco.String(20))
  ano = banco.Column(banco.Float)
  cor = banco.Column(banco.String(10))
  combustivel = banco.Column(banco.String(20))
  valor = banco.Column(banco.Float)
  
  def __init__(self, veiculo_id, modelo, placa, marca, ano, cor, combustivel, valor):
    self.veiculo_id = veiculo_id
    self.modelo = modelo
    self.placa = placa
    self.marca = marca
    self.ano = ano
    self.cor = cor
    self.combustivel = combustivel
    self.valor = valor
  def json(self):
    return {
      'veiculo_id': self.veiculo_id,
      'modelo': self.modelo,
      'placa': self.placa,
      'marca': self.marca,
      'ano': self.ano,
      'cor': self.cor,
      'combustivel': self.combustivel,
      'valor': self.valor
    }

  @classmethod
  def find_veiculo(cls, veiculo_id):
    veiculo = cls.query.filter_by(veiculo_id=veiculo_id).first()
    if veiculo:
      return veiculo
    return None

  def save_veiculo(self):
    banco.session.add(self)
    banco.session.commit()

  def update_veiculo(self, modelo, placa, marca, ano, cor, combustivel, valor):
    self.modelo = modelo
    self.placa = placa
    self.marca = marca
    self.ano = ano
    self.cor = cor
    self.combustivel = combustivel
    self.valor = valor

  def delete_veiculo(self):
    banco.session.delete(self)
    banco.session.commit()