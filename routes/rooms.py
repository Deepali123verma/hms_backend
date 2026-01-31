from flask_restx import Namespace, Resource, fields
from flask import request
from models import db, Room

api = Namespace("rooms", description="Room Management APIs")

room_model = api.model("Room", {
    "room_number": fields.String(required=True),
    "room_category": fields.String(required=True),
    "price": fields.Float(required=True),
    "status": fields.String(required=True, enum=["available","booked","occupied"])
})

@api.route("/")
class RoomList(Resource):
    def get(self):
        rooms = Room.query.all()
        return [{"room_id": r.room_id, "room_number": r.room_number, "room_category": r.room_category,
                 "price": float(r.price), "status": r.status} for r in rooms]

    @api.expect(room_model)
    def post(self):
        data = request.json
        room = Room(**data)
        db.session.add(room)
        db.session.commit()
        return {"message": "Room added successfully"}, 201
