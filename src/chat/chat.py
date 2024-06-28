import random
from socket import SocketIO
from string import ascii_letters
from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import current_user
from flask_socketio import rooms


from database import db

chat = Blueprint('chat', __name__, template_folder='templates', static_folder='static')
