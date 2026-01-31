from flask_restx import Namespace, Resource, fields
from flask import request
from models import db, Staff

api = Namespace("staff", description="Staff Management APIs")

staff_model = api.model("Staff", {
    "name": fields.String(required=True),
    "role": fields.String(required=True),
    "contact": fields.String(required=True)
})

@api.route("/")
class StaffList(Resource):
    def get(self):
        staff = Staff.query.all()
        return [{"staff_id": s.staff_id, "name": s.name, "role": s.role, "contact": s.contact} for s in staff]

    @api.expect(staff_model)
    def post(self):
        data = request.json
        staff = Staff(**data)
        db.session.add(staff)
        db.session.commit()
        return {"message": "Staff added successfully"}, 201
