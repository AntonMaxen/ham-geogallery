from flask import Blueprint
# from app.ui import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return 'Index'
