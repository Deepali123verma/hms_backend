from flask_restx import Namespace, Resource, fields
from flask import request
from models import db, Billing

api = Namespace("billing", description="Billing APIs")

billing_model = api.model("Billing", {
    "booking_id": fields.Integer(required=True),
    "total_amount": fields.Float(required=True),
    "payment_status": fields.String(required=True)
})

@api.route("/")
class BillingList(Resource):
    def get(self):
        bills = Billing.query.all()
        return [{"bill_id": b.bill_id, "booking_id": b.booking_id,
                 "total_amount": float(b.total_amount), "payment_status": b.payment_status,
                 "billing_date": str(b.billing_date)} for b in bills]

    @api.expect(billing_model)
    def post(self):
        data = request.json
        bill = Billing(**data)
        db.session.add(bill)
        db.session.commit()
        return {"message": "Bill created successfully"}, 201
