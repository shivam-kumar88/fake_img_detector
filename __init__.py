from flask import Flask
import flask

app = flask(__name__)

app.config.from_object("config.DevelopmentConfig")

from app import views