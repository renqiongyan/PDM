from flask import Blueprint

bp_worker = Blueprint('bp_transport', __name__)

from . import views

#


