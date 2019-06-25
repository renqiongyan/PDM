from flask import Blueprint

bp_shopowner = Blueprint('bp_shopowner', __name__)

from . import views