from flask import Blueprint

controllers = Blueprint('controllers', __name__)

from . import views
from . import challenge
from . import profile
from . import login
from . import search
from . import register
