from flask import Blueprint

bp_welcome = Blueprint('bp_welcome', __name__)

from . import views