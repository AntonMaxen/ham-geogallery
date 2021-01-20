from flask import Blueprint, render_template, url_for
import app.bl.location_controller as lc
import app.bl.utility_controller as uc
bp = Blueprint('map', __name__, url_prefix='/map')

@bp.route('/')
def index():
    return render_template('map.html')


if __name__ == '__main__':
    pass
