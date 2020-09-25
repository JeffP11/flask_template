import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('bp_test', __name__, url_prefix='/bp_test')

@bp.route('/post/', methods=['GET', 'POST'])
def testing():
    data_server = {
        'server': 'servidor',
        'database': 'database'
    }
    
    data_date = {
        'date': 'date'
    }

    if request.method == 'POST':
        return jsonify(data_date)
    elif request.method == 'GET':
        return jsonify(data_server)