from flask import Blueprint

bp_shopowners = Blueprint('bp_shopowners', __name__)

from . import views