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
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Retrievse the locale of a web page """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        print(locale)
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """ Home/index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
