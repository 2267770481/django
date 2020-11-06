from flask import Blueprint, request, current_app

bp = Blueprint('index', __name__)


@bp.route('/index')
def index():
    current_app.logger.debug('测试日志')
    current_app.logger.info('测试日志')
    current_app.logger.warning('测试日志')
    current_app.logger.error('测试日志')
    current_app.logger.critical("测试日志")
    return 'index'


@bp.route('/tips')
def tips():
    args = request.args.to_dict()
    print(args)
    msg = args.get('tips', None)
    return f'{msg}'
