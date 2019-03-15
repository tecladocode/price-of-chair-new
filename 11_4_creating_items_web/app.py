from flask import Flask
from views.items import item_blueprint

app = Flask(__name__)

app.register_blueprint(item_blueprint, url_prefix="/items")

if __name__ == "__main__":
    app.run(debug=True)
