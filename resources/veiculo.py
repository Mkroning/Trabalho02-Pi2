from flask_restful import Resource, reqparse
from models.veiculo import VeiculoModel

veiculos = []

class Veiculos(Resource):
  def get(self):
    return{'Veiculos': 'Meus Veiculos'}

class Veiculo(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('modelo')
  argumentos.add_argument('placa')
  argumentos.add_argument('marca')
  argumentos.add_argument('ano')
  argumentos.add_argument('cor')
  argumentos.add_argument('combustivel')
  argumentos.add_argument('valor')

  def find_veiculo(veiculo_id):
    for veiculo in veiculos:
      if veiculo['veiculo_id'] == veiculo_id:
        return veiculo
    return None

  def get(self, veiculo_id):
    veiculo = Veiculo.find_veiculo(veiculo_id)
    if veiculo:
      return veiculo
    return {'message': 'Car not found'}, 404 #notFound

  def post(self, veiculo_id):
    dados = Veiculo.argumentos.parse_args()

    veiculo_objeto = VeiculoModel(veiculo_id, **dados)
    novo_veiculo = veiculo_objeto.json()

    veiculos.append(novo_veiculo)
    return novo_veiculo, 200

  def put(self, veiculo_id):
    dados = Veiculo.argumentos.parse_args()

    veiculo_objeto = VeiculoModel(veiculo_id, **dados)
    novo_veiculo = veiculo_objeto.json()

    veiculo = Veiculo.find_veiculo(veiculo_id)
    if veiculo:
      hotel.update(novo_veiculo)
      return novo_veiculo, 200
    veiculos.append(novo_veiculo)
    return novo_veiculo, 201


  def delete(self, veiculo_id):
    global veiculos
    veiculos = [veiculo for veiculo in veiculos if veiculo['veiculo_id'] != veiculo_id]
    return {'message': 'Veiculo Deleted'}