from flask import Blueprint

bp = Blueprint("users",
               __name__,
               template_folder="templates",
               #url_prefix="/users2"
               )

from . import views