from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from routes import bp, api

from routes.auth import api as auth_api
from routes.rooms import api as rooms_api
from routes.booking import api as booking_api
from routes.billing import api as billing_api
from routes.staff import api as staff_api
from routes.restaurant import api as restaurant_api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Register blueprint first
    app.register_blueprint(bp, url_prefix="/api")

    # Register all namespaces
    api.add_namespace(auth_api, path="/auth")
    api.add_namespace(rooms_api, path="/rooms")
    api.add_namespace(booking_api, path="/booking")
    api.add_namespace(billing_api, path="/billing")
    api.add_namespace(staff_api, path="/staff")
    api.add_namespace(restaurant_api, path="/restaurant")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    
@app.route("/api/health")
def health():
    return {"status": "ok"}

