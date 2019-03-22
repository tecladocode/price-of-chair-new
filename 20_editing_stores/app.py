from flask import Flask
from views.alerts import alert_blueprint
from views.stores import store_blueprint

app = Flask(__name__)

app.register_blueprint(alert_blueprint, url_prefix="/alerts")
app.register_blueprint(store_blueprint, url_prefix="/stores")

if __name__ == "__main__":
    app.run(debug=True)
