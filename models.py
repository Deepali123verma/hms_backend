from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    bookings = db.relationship("Booking", backref="user", lazy=True)

class Room(db.Model):
    __tablename__ = "rooms"
    room_id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), nullable=False)
    room_category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    bookings = db.relationship("Booking", backref="room", lazy=True)

class Booking(db.Model):
    __tablename__ = "bookings"
    booking_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.room_id"), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    booking_status = db.Column(db.String(20), nullable=False)

    billing = db.relationship("Billing", backref="booking", uselist=False)

class Billing(db.Model):
    __tablename__ = "billing"
    bill_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.booking_id"), nullable=False)
    total_amount = db.Column(db.Numeric(10,2), nullable=False)
    payment_status = db.Column(db.String(20), nullable=False)
    billing_date = db.Column(db.DateTime, server_default=db.func.now())

class Staff(db.Model):
    __tablename__ = "staff"
    staff_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(15), nullable=False)

class RestaurantMenu(db.Model):
    __tablename__ = "restaurant_menu"
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    price = db.Column(db.Numeric(10,2))
    availability = db.Column(db.Boolean, default=True)


class RestaurantOrder(db.Model):
    __tablename__ = "restaurant_orders"
    order_id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.Integer, db.ForeignKey("bookings.booking_id"))
    item_id = db.Column(db.Integer, db.ForeignKey("restaurant_menu.item_id"))
    quantity = db.Column(db.Integer)
    total_price = db.Column(db.Numeric(10,2))
    order_status = db.Column(db.String(20))
