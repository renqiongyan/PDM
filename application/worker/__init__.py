from flask import Blueprint

bp_worker = Blueprint('bp_worker', __name__)

from . import views