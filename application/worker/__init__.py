from flask import Blueprint

bp_transport = Blueprint('bp_transport', __name__)

from . import views

#


