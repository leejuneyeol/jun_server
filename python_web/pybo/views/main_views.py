from flask import Blueprint, url_for, abort
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/500')
def error500():
    abort(500)
    
@bp.route('/files')
def files():
    return redirect('pybo\templates\files.html')
    
@bp.route('/')
def index():
    return redirect(url_for('question._list'))