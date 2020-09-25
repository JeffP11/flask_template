import functools

from flask import Blueprint, request, jsonify

bp = Blueprint('bp_test', __name__, url_prefix='/bp_test')

@bp.route('/test/', methods=['GET', 'POST'])
def testing():

    data = request.args

    data_server = {
        'server': data.get('server'),
        'database': data.get('database')
    }
    
    data_date = {
        'date': data.get('date')
    }

    if request.method == 'POST':
        return jsonify(data_date)
        
    elif request.method == 'GET':
        return jsonify(data_server)