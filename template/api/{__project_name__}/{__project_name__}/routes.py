from . import app
from .views.example import root


app.addroute(root, "/", methods=["GET"])

