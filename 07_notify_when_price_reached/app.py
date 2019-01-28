from models.item import Item
from models.alert import Alert

ipad = Item(
    "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-512gb/space-grey/p3834614",
    "p",
    {"class": "price price--large"}
)

ipad.save_to_mongo()

alert = Alert(ipad._id, 1000)
alert.save_to_mongo()