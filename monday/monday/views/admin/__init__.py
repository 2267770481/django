from flask import Blueprint
from .views import AddCmpInfo, AddPneInfo, FindPhone

bp = Blueprint('admin', __name__, url_prefix='/admin')

bp.add_url_rule('/add_company', view_func=AddCmpInfo.as_view('add_company'), methods=["GET", "POST"])
bp.add_url_rule('/add_phone', view_func=AddPneInfo.as_view('add_phone'), methods=["GET", "POST"])
bp.add_url_rule('/find_phone', view_func=FindPhone.as_view('find_phone'), methods=["GET", "POST"])
