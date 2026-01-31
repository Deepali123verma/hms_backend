from flask_restx import Namespace, Resource, fields
from flask import request
from models import db, Booking

api = Namespace("booking", description="Booking APIs")

booking_model = api.model("Booking", {
    "user_id": fields.Integer(required=True),
    "room_id": fields.Integer(required=True),
    "check_in": fields.String(required=True),
    "check_out": fields.String(required=True),
    "booking_status": fields.String(required=True)
})

@api.route("/")
class BookingList(Resource):
    def get(self):
        bookings = Booking.query.all()
        return [{"booking_id": b.booking_id, "user_id": b.user_id, "room_id": b.room_id,
                 "check_in": str(b.check_in), "check_out": str(b.check_out),
                 "booking_status": b.booking_status} for b in bookings]

    @api.expect(booking_model)
    def post(self):
        data = request.json
        booking = Booking(**data)
        db.session.add(booking)
        db.session.commit()
        return {"message": "Booking created successfully"}, 201
