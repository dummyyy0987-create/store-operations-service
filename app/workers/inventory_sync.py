import time
from db.connection import get_db

def sync_inventory():
    """
    Pulls warehouse inventory and pushes updates
    to store_inventory table.
    """
    while True:
        db = get_db()
        print("Syncing inventory...")
        # Dummy logic
        time.sleep(600)
