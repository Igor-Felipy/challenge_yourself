from flask import Blueprint

controllers = Blueprint("controllers", __name__)

from . import search
from . import login
from . import challenge
from . import profile