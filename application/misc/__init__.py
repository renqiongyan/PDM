from flask import Blueprint

bp_misc = Blueprint('bp_misc', __name__)

from . import views