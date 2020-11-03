from flask import Blueprint, request

bp = Blueprint('index', __name__)


@bp.route('/index')
def index():
    return 'index'


@bp.route('/tips')
def tips():
    args = request.args.to_dict()
    print(args)
    msg = args.get('tips', None)
    return f'{msg}'
