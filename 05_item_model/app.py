from models.item import Item

ipad = Item(
    "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-512gb/space-grey/p3834614",
    "p",
    {"class": "price price--large"}
)

print(ipad.load_price())
