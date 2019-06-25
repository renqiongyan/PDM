from flask import Blueprint

bp_auth = Blueprint('bp_auth', __name__)

from . import views