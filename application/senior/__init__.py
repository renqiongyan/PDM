from flask import Blueprint

bp_senior = Blueprint('bp_senior', __name__)

from . import views