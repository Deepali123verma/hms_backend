from flask_restx import Namespace, Resource, fields
from flask import request
from models import db, RestaurantMenu, RestaurantOrder

api = Namespace("restaurant", description="Restaurant APIs")

menu_model = api.model("Menu", {
    "item_name": fields.String,
    "category": fields.String,
    "price": fields.Float,
    "availability": fields.Boolean
})

order_model = api.model("Order", {
    "booking_id": fields.Integer,
    "item_id": fields.Integer,
    "quantity": fields.Integer,
    "total_price": fields.Float,
    "order_status": fields.String
})

@api.route("/menu")
class Menu(Resource):
    def get(self):
        items = RestaurantMenu.query.all()
        return [{
            "item_id": i.item_id,
            "item_name": i.item_name,
            "category": i.category,
            "price": float(i.price),
            "availability": i.availability
        } for i in items]

    @api.expect(menu_model)
    def post(self):
        item = RestaurantMenu(**request.json)
        db.session.add(item)
        db.session.commit()
        return {"message": "Menu item added"}, 201

@api.route("/order")
class Order(Resource):
    def get(self):
        orders = RestaurantOrder.query.all()
        return [{
            "order_id": o.order_id,
            "booking_id": o.booking_id,
            "item_id": o.item_id,
            "quantity": o.quantity,
            "total_price": float(o.total_price),
            "order_status": o.order_status
        } for o in orders]   # ✅ yeh bracket missing tha

    @api.expect(order_model)
    def post(self):
        order = RestaurantOrder(**request.json)
        db.session.add(order)
        db.session.commit()
        return {"message": "Food order placed"}, 201
