from flask_restful import Resource, reqparse
from models.veiculo import VeiculoModel
from flask_jwt_extended import jwt_required

veiculos = []

class Veiculos(Resource):
  def get(self):
    return{'Veiculos': [veiculo.json for veiculo in VeiculoModel.query.all()]}

class Veiculo(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('modelo', type=str, required=True, help="O campo 'modelo' não pode ser deixado em branco")
  argumentos.add_argument('placa')
  argumentos.add_argument('marca')
  argumentos.add_argument('ano', type=float, required=True, help="O campo 'ano' não pode ser deixado em branco")
  argumentos.add_argument('cor')
  argumentos.add_argument('combustivel')
  argumentos.add_argument('valor', type=float, required=True, help="O campo 'valor' não pode ser deixado em branco")

  def get(self, veiculo_id):
    veiculo = VeiculoModel.find_veiculo(veiculo_id)
    if veiculo:
      return veiculo.json()
    return {'message': 'Car not found'}, 404 #notFound

  @jwt_required
  def post(self, veiculo_id):
    if VeiculoModel.find_veiculo(veiculo_id):
      return{"message":"Veiculo id'{}'already exists.".format(veiculo_id)}, 400
    

    dados = Veiculo.argumentos.parse_args()

    veiculo_objeto = VeiculoModel(veiculo_id, **dados)
    try:
      veiculo.save_veiculo()
    except:
      return{'message': 'An internal error ocurred trying to save veiculo'}, 500
    return veiculo.json()

  @jwt_required
  def put(self, veiculo_id):
    dados = Veiculo.argumentos.parse_args()
       
    veiculo_encontrado = VeiculoModel.find_veiculo(veiculo_id)
    if veiculo_encontrado:
      veiculo_encontrado.update_veiculo(**dados)
      veiculo_encontrado.save_veiculo()
      return veiculo_encontrado.json(), 200
    veiculo = VeiculoModel(veiculo_id, **dados)
    try:
      veiculo.save_veiculo()
    except:
      return {'message': 'An internal error ocurred trying to save veiculo'}, 500
    return veiculo.json(), 201

  @jwt_required
  def delete(self, veiculo_id):
    veiculo = VeiculoModel.find_veiculo(veiculo_id)
    if veiculo:
      try:
        veiculo.delete_veiculo()
      except:
        return {'message': 'An error ocurred trying to delete veiculo'}, 500
      return {'message': 'Veiculo Deleted'}
    return {'message':'Veiculo not found'},404