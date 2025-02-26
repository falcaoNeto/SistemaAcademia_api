from flask import Blueprint

home_route = Blueprint('home', __name__)


@home_route.route('/')
def home():
    return 'home'