from flask import Blueprint

bp = Blueprint("user_name",
               __name__,
               template_folder="templates/templates",
               #url_prefix="/users2"
               )

from . import views