import json
from flask import Blueprint, render_template, request, redirect, url_for
from models.alert import Alert

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    alerts = Alert.all()
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def create_alert():
    if request.method == 'POST':
        item_id = request.form['item_id']
        price_limit = request.form['price_limit']

        Alert(item_id, price_limit).save_to_mongo()

    # What happens if it's a GET request
    return render_template("alerts/new_alert.html")
