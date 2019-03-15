import json
from flask import Flask, render_template, request
from models.item import Item


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_item():
    if request.method == 'POST':
        url = request.form['url']
        tag_name = request.form['tag_name']
        query = json.loads(request.form['query'])

        Item(url, tag_name, query).save_to_mongo()

    return render_template("items/new_item.html")

if __name__ == "__main__":
    app.run(debug=True)
