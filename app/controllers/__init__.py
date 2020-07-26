from flask import Blueprint


controllers = Blueprint("controllers", __name__)

from . import challenge
from . import feed
from . import login
from . import profile
from . import register 
from . import search
