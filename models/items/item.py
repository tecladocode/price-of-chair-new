from dataclasses import dataclass, field
from typing import Dict
import uuid
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
from models.model import Model
from common.database import Database
from models.stores.store import Store


@dataclass(eq=False)
class Item(Model):
    collection: str = field(init=False, default="items")
    name: str
    url: str
    price: float = None
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    selector: str = field(init=False)

    def __post_init__(self):
        store = Store.find_by_url(self.url)
        self.selector = store.selector

    def load_price(self):
        session = HTMLSession()
        request = session.get(self.url)
        # Although not working well at the moment.
        # in the future we will be able to do request.html.render() in order
        # to evaluate JavaScript, which greatly increases the
        # capabilities of this project.
        # https://github.com/thp/urlwatch/pull/310
        # and https://github.com/kennethreitz/requests-html/issues/155
        element = request.html.find(self.selector, first=True)
        string_price = element.text.strip()

        pattern = re.compile(r"(\d+.\d+)")
        match = pattern.search(string_price)
        self.price = float(match.group(1))
        return self.price

    def json(self):
        return {
            "_id": self._id,
            "name": self.name,
            "url": self.url,
            "price": self.price,
        }
