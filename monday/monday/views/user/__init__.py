from flask import (Blueprint, render_template, session)

bp = Blueprint('user', __name__, url_prefix='/user')

from .views import Register

bp.add_url_rule('/register', view_func=Register.as_view('logged'), methods=['POST', 'GET'])
