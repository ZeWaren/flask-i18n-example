# Flask i18n example

This is a roughly and badly documented test app that shows how to use `Flask-Babel` and `gettext` to translate a Flask app.

Its most interesting part is the translation of the javascript content, since no coherent documentation is to be found on the internet regarding this subject.

## Create the application
Create a virtual env as usual:

    # (FreeBSD commands)
    make -C /usr/ports/devel/py-virtualenv install clean
    virtualenv -p /usr/local/bin/python3.4 venv
    source venv/bin/activate.csh

Install flask:

    pip install flask

Create a route that outputs a template, add some js files.

## Install Flask-Babel
Install flask-babel:

    pip install flask-babel

Instantiate and configure the package in your app file:

    from flask.ext.babel import Babel
    babel = Babel(app)

Add some text everywhere in your app.

## Extract the texts and create the translation files

Extract the texts from the files (see `babel.cfg`):

    venv/bin/pybabel extract -F babel.cfg -o messages.pot .

Create or update your translation files: 

    venv/bin/pybabel init -i messages.pot -d translations -l fr

OR

    venv/bin/pybabel update -i messages.pot -d translations


Compile the translations:

    venv/bin/pybabel compile -d translations

## Configure jsgettext to translate content in javascript files

Get `Gettext.js` from and add it to the project: [https://sourceforge.net/projects/jsgettext.berlios/](https://sourceforge.net/projects/jsgettext.berlios/)

See file `statis/js/scripts.js` to see how to use it.

### Use the PO/MO files

Copy the file somewhere in the static folder and inform `jsgettext` that the translations are in them:

    <link rel="gettext" type="application/x-po" href="{{ url_for('static', filename='translations/fr.po') }}">

### Use JSON files

Install `pojson`.

    pip install pojson


Convert the PO file to JSON:


    echo -n "{'flask-i18n-example': " > static/translations/fr.json
    venv/bin/pojson translations/fr/LC_MESSAGES/messages.po >> static/translations/fr.json
    echo "}" >> static/translations/fr.json


Inform `jsgettext` that the translation are in the JSON file:

    <link rel="gettext" type="application/json" href="{{ url_for('static', filename='translations/fr.json') }}">

