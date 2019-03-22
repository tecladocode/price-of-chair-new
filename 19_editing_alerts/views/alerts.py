import json
from flask import Blueprint, render_template, request, redirect, url_for
from models.alert import Alert
from models.store import Store
from models.item import Item

alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.route('/')
def index():
    alerts = Alert.all()
    return render_template('alerts/index.html', alerts=alerts)


@alert_blueprint.route('/new', methods=['GET', 'POST'])
def create_alert():
    if request.method == 'POST':
        item_url = request.form['item_url']

        store = Store.find_by_url(item_url)
        item = Item(item_url, store.tag_name, store.query)
        item.load_price()
        item.save_to_mongo()

        alert_name = request.form['name']
        price_limit = request.form['price_limit']

        Alert(alert_name, item._id, price_limit).save_to_mongo()

    # What happens if it's a GET request
    return render_template("alerts/new_alert.html")



@alert_blueprint.route('/edit/<string:alert_id>', methods=['GET', 'POST'])
def edit_alert(alert_id):
    if request.method == 'POST':
        price_limit = float(request.form['price_limit'])

        alert = Alert.get_by_id(alert_id)
        alert.price_limit = price_limit
        alert.save_to_mongo()

        return redirect(url_for('.index'))

    # What happens if it's a GET request
    return render_template("alerts/edit_alert.html", alert=Alert.get_by_id(alert_id)) 
