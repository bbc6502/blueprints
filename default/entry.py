import os
from flask import Blueprint, render_template
import blueprints

bp_dir = os.path.dirname(__file__)
templates_dir = os.path.join(bp_dir, 'templates')
bp = Blueprint('default', __name__, template_folder=templates_dir, url_prefix='/')


@bp.route('/')
def welcome():
    context = {
        'title': 'Blueprints',
        'blueprints': blueprints.blueprints,
    }
    return render_template('welcome.html', **context)
