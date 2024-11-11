#!/usr/bin/env python3
""" Basic flask app """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configuration class for Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Configuration for Flask app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Retrievse the locale of a web page """
    return request.accept_languages.best_match(app.config["Languages"])


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
