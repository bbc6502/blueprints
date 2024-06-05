import os
from flask import Blueprint, render_template
"""
Welcome blueprint
"""

bp_dir = os.path.dirname(__file__)
templates_dir = os.path.join(bp_dir, 'templates')
bp = Blueprint('welcome', __name__, template_folder=templates_dir)


@bp.route('/')
def welcome():
    context = {'hello': 'world'}
    return render_template('welcome/welcome.html', **context)
