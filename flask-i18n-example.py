import flask
app = flask.Flask(__name__)

from werkzeug.contrib.fixers import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)

from flask.ext.babel import Babel
babel = Babel(app)

from flask import render_template
from flask.ext.babel import gettext as _, ngettext

@babel.localeselector
def get_locale():
    return 'fr'

@app.route("/")
def index():
    brittany = _('Brittany')
    france = _('France')
    return render_template('index.html',
                           some_text=_("I am a sausage."),
                           best_part=_("%(part)s is the best part of %(country)s.", part=brittany, country=france),
                           singular=ngettext('I bought a garlic glove this morning.', 'I bought %(num)d garlic gloves this morning.', 1),
                           plural=ngettext('I bought a garlic glove this morning.', 'I bought %(num)d garlic gloves this morning.', 42))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
