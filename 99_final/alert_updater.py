from common.database import Database
from models.alert import Alert

Database.initialize()

alerts_needing_update = Alert.find_needing_update(10)

for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()
