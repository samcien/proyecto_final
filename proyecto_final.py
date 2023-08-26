from flask import Flask, render_template, request, jsonify
from api import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='/api')


citas = []

@app.route('/')
def index():
    return render_template('index.html', citas=citas)

@app.route('/agregar_cita', methods=['POST'])
def agregar_cita():
    nombre = request.form.get('nombre')
    fecha = request.form.get('fecha')
    hora = request.form.get('hora')
    citas.append({'nombre': nombre, 'fecha': fecha, 'hora': hora})
    return render_template('index.html', citas=citas)

if __name__ == '__main__':
    app.run(debug=True)

