from common.database import Database
from models.alerts.alert import Alert

Database.initialize()

alerts_needing_update = Alert.find_needing_update()

for alert in alerts_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()
