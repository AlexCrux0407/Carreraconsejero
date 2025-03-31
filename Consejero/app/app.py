from flask import Flask, jsonify, render_template, request
import json
from hardware_analyzer import get_hardware_info
from career_recommender import get_career_recommendation

app = Flask(__name__)

@app.route('/')
def index():
    """Renderiza la página principal"""
    return render_template('index.html')

@app.route('/analyze', methods=['GET'])
def analyze():
    """Analiza el hardware y devuelve los resultados"""
    try:
        # Obtener información del hardware
        hardware_info = get_hardware_info()
        
        # Obtener recomendación de carrera
        career = get_career_recommendation(hardware_info)
        
        # Preparar respuesta
        response = {
            'status': 'success',
            'hardware': hardware_info,
            'career': career
        }
        
        return render_template('results.html', hardware=hardware_info, career=career)
    
    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(error_response), 500

@app.route('/api/hardware', methods=['GET'])
def get_hardware():
    """API endpoint para obtener solo información del hardware"""
    try:
        hardware_info = get_hardware_info()
        return jsonify(hardware_info)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/career', methods=['GET'])
def get_career():
    """API endpoint para obtener solo la recomendación de carrera"""
    try:
        hardware_info = get_hardware_info()
        career = get_career_recommendation(hardware_info)
        return jsonify(career)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)