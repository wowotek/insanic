from . import app
from .views.example import root


app.add_route(root, "/", methods=["GET"])

