from dataclasses import dataclass, field
from typing import List, Dict
from flask import current_app
import uuid
import datetime
import requests
from models.model import Model
from common.database import Database
from models.item import Item


@dataclass(eq=False)
class Alert(Model):
    collection: str = field(init=False, default="alerts")
    user_email: str
    price_limit: str
    item_id: str
    active: bool = True
    last_checked: datetime.datetime = field(default_factory=datetime.datetime.utcnow)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)

    def send(self) -> requests.Request:
        return requests.post(
            current_app.config.MAILGUN_URL,
            auth=("api", current_app.config.MAILGUN_API_KEY),
            data={
                "from": current_app.config.MAILGUN_FROM,
                "to": self.user_email,
                "subject": "Price limit reached for {}".format(self.item.name),
                "text": "We've found a deal! ({}).".format(self.item.url),
            },
        )

    @classmethod
    def find_needing_update(cls, minutes_since_update: int) -> List["Alert"]:
        last_updated_limit = datetime.datetime.utcnow() - datetime.timedelta(
            minutes=minutes_since_update
        )
        return [
            cls(**elem)
            for elem in Database.find(
                cls.collection,
                {"last_checked": {"$lte": last_updated_limit}, "active": True},
            )
        ]

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "price_limit": self.price_limit,
            "last_checked": self.last_checked,
            "user_email": self.user_email,
            "item_id": self.item._id,
            "active": self.active,
        }

    def load_item_price(self) -> float:
        self.item.load_price()
        self.last_checked = datetime.datetime.utcnow()
        self.item.save_to_mongo()
        self.save_to_mongo()
        return self.item.price

    def send_email_if_price_reached(self) -> None:
        if self.item.price < self.price_limit:
            self.send()

    @classmethod
    def find_by_user_email(cls, user_email: str) -> List["Alert"]:
        return cls.find_many_by("user_email", user_email)

    def deactivate(self) -> None:
        self.active = False
        self.save_to_mongo()

    def activate(self) -> None:
        self.active = True
        self.save_to_mongo()
