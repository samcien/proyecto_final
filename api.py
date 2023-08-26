from flask import Blueprint, jsonify

# Crea un blueprint para la API
api_blueprint = Blueprint('api', __name__)

# Endpoint para obtener citas
@api_blueprint.route('/citas', methods=['GET'])
def obtener_citas():
    return jsonify(citas)
