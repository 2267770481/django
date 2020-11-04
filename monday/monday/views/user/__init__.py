from flask import (Blueprint, render_template, session)

bp = Blueprint('user', __name__, url_prefix='/user')

from .views import Logged

bp.add_url_rule('/register', view_func=Logged.as_view('logged'), methods=['POST', 'GET'])
