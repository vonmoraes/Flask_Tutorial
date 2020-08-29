from flask import (
    Flask, redirect, url_for, render_template, request, session, flash
)
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALQUEMY_DATABASE_URI'] = 'sqlite:///storage.db' # pode ser um postgres

# os controllers utilizam a var app por isso é importado depois
from app.controllers import default