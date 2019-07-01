import os

secret_key = os.getenv("FLASK_SECRET_KEY")
db_url = os.getenv("FLASK_DB")

admin_pin = os.getenv("FLASK_ADMIN_PIN")