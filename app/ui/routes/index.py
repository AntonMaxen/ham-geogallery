from flask import Blueprint, redirect

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return redirect('/map')
